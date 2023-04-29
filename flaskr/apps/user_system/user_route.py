# from __init__ import app
from flaskr.apps.user_system.user_model import *
from flaskr.apps.user_system.user_form import *
from flask import render_template, request, url_for, redirect, session

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route("/register",methods=["GET","POST"])
def register():
    if request.method == 'GET':
        form_register = RegistrationForm()
        return render_template('auth/register.html',form_register=form_register) # TODO

    if request.method == 'POST':
        form_register = RegistrationForm(formdata=request.form)
        if form_register.validate():
            info_register(form_register.data)
            return redirect(url_for('auth.login'))
        else:
            print(form_register.errors, "Error Message")
            return render_template('auth/register.html',form_register=form_register) # TODO
        
@bp.route("/userinfo", methods=("GET", "POST"))
def userinfo():
    #return render_template("auth/userinfo.html")
    if request.method == 'GET':
        form_modify = InfoModifyForm()
        return render_template("auth/userinfo.html",form_modify=form_modify)
    
    if request.method == 'POST':
        form_modify = InfoModifyForm(formdata=request.form)
        if form_modify.validate():
            infoModify(session['user_uid'], form_modify.data)
            return redirect(url_for("user.userinfo"))
        else:
            print(form_modify.errors, "Error Message")
            return render_template("auth/userinfo.html",form_modify=form_modify)
