import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    '''
        All the view function that need to be login required should be decorated by this function
        If the user is not login, redirect to the login page
    '''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        db=get_db()
        db.execute("SELECT * FROM user WHERE UID = \"{}\"".format(user_id))
        g.user = (
            db.fetchone()
        )


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        print("password: ",password," len: ",len(password))
        db = get_db()
        query = "INSERT INTO user (email, password) VALUES (\"{}\",\"{}\")".format(email,password)
        # todo : set UID auto increment, set the password length to 102
        error = None

        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(query)
                db.connection.commit()
            except db.IntegrityError:
                # The email was already taken, which caused the
                # commit to fail. Show a validation error.
                error = f"EMAIL: {email} is already registered."
            else:
                # Success, go to the login page.
                return redirect(url_for("auth.login"))

        flash(error)
    return render_template("auth/register.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        db = get_db()
        error = None
        query = "SELECT * FROM user WHERE email=\"{s}\"".format(s=email)
        
        db.execute(query)
        result=db.fetchone()
        print(result)
        if result is None:
            error = "Incorrect email."
        else:
            user_UID, user_password_hashed, user_email  = result
            if not check_password_hash( user_password_hashed, password):
                error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user_UID
            return redirect(url_for("index"))

        flash(error)
    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))