from __init__ import app
from flaskr.apps.user_system.user_models import *
from flaskr.apps.user_system.user_forms import *
from flask import render_template, request, url_for, redirect, session

@route("/info/modify",method=["GET","POST"])
def info_modify():
    if request.method == 'GET':
        form_modify = InfoModifyForm()
        return render_template('',form_modify=form_modify)
    else:
        form_modify = InfoModifyForm(formdata=request.form)
        if form.validate():
            infoModify(session['user_id'], form.data)
            return redirect(url_for('info'))
        else:
            print(form.errors, "Error Message")

            return render_template("info.html",info_form=form_modify)
        
@route("/register",method=["GET","POST"])
def info_register():
    if request.method == 'GET':
        form = RegistrationForm()
        return render_template('',form_register=form_register) # TODO

    if request.method == 'POST':
        form = RegistrationForm()
        if form.validate():
            info_register(session['user_id'], form.data)
            return redirect(url_for('auth.login'))
        else:
            print(form.errors, "Error Message")
            return render_template('',form_register=form_register) # TODO