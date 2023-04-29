from flaskr.apps.order_system.order_model import *
from flaskr.apps.order_system.order_form import *
from flask import render_template, request, url_for, redirect, session
from flaskr.apps.auth import login_required
from flaskr.apps.search_system.search import get_search_result

bp = Blueprint('order', __name__)
       
@bp.route("/create_order",methods=["GET","POST"])  # TODO test
@login_required
def create_order():
    if request.method == 'GET':
        form_create_order = OrderInfoForm()
        return render_template('order/create_order.html',form_create_order=form_create_order)
    else:
        form_create_order = OrderInfoForm(formdata=request.form)
        print(form_create_order.startTime)
        print(form_create_order.dueTime)
        if form_create_order.validate():
            order_create(session['user_uid'], form_create_order.data)
            return redirect(url_for('order.index')) # TODO: redirect url
        else:
            print(form_create_order.errors, "Error Message")

            return render_template("order/create_order.html",form_create_order=form_create_order) # TODO: render html template

@bp.route("/",methods=["GET","POST"])
def index():
    if request.method == 'GET':
        oldOID = return_latest_ID(0)
        g.order = {}
        orderlist=[]
        for OID in oldOID:
            orderlist.append((OID,getFormData(OID)))
        g.order["orderlist"] = orderlist
        g.order["oldID"] = oldOID
        g.order["count"] = 1
        return render_template('index.html')
    
    if request.method == 'POST':
        oldOID = return_latest_ID(g.order['count'])
        g.order['count'] = g.order['count'] + 1
        orderlist = []
        for OID in oldOID:
            orderlist.append((OID,getFormData(OID)))
        g.order["orderlist"] = orderlist
        g.order["oldID"] = oldOID
        return render_template("index.html")
        
        

@bp.route("/search_order/<token>",methods=["GET"])
def search_order(token):
    search_result_form=get_search_result(token)
    print("order_rout: search_result\n")
    print(search_result_form)
    return render_template('order/search_order.html',search_result_form=search_result_form)


    