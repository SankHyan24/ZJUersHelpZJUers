from flaskr.apps.order_system.order_model import *
from flaskr.apps.order_system.order_form import *
from flask import render_template, request, url_for, redirect, session
from flaskr.apps.auth import login_required

bp = Blueprint('order', __name__)
       
@bp.route("/create_order",methods=["GET","POST"])  # TODO test
@login_required
def create_order():
    if request.method == 'GET':
        form_create_order = OrderInfoForm()
        return render_template('',form_create_order=form_create_order)
    else:
        form_create_order = OrderInfoForm(formdata=request.form)
        if form_create_order.validate():
            order_create(session['user_id'], form_create_order.data)
            return redirect(url_for('')) # TODO: redirect url
        else:
            print(form_create_order.errors, "Error Message")

            return render_template("",info_form=form_create_order) # TODO: render html template

@bp.route("/",methods=["GET","POST"])
def index():
    newOID = return_newest_ID()
    for OID in newOID:
        g.order[OID] = getFormData(OID)
        g.newID = newOID
    return render_template('index.html')





@bp.route("/search_order/<int:token>",methods=["GET"])
def search_order(token):
    search_result_form=get_search_result(token)
    return render_template('search.html',search_result_form=search_result_form)


    