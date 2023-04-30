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
            return redirect(url_for('order.index',pageNumber = 1)) # TODO: redirect url
        else:
            print(form_create_order.errors, "Error Message")

            return render_template("order/create_order.html",form_create_order=form_create_order) # TODO: render html template

@bp.route("/<int:pageNumber>",methods=["GET"])
@login_required
def index(pageNumber):
    if request.method == 'GET':
        oldOID = return_latest_ID(pageNumber)
        g.order = {}
        orderlist=[]
        for OID in oldOID:
            orderlist.append((OID,getFormData(OID[0])))
        g.order["orderlist"] = orderlist
        g.order["oldID"] = oldOID
        g.order["pageNumber"] = pageNumber
        return render_template('index.html')

@bp.route("/",methods=["GET"])
def null_index():
    user_uid = session.get("user_uid")
    if user_uid is None:
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('order.index',pageNumber=1))
        
@bp.route("/search_order/<token>",methods=["GET"])
@login_required
def search_order(token):
    search_result_form=get_search_result(token)
    # print(search_result_form)
    g.search = {}
    searchlist=[]
    for order in search_result_form:
        searchlist.append((order[0],getFormData(order[0])))
    print("searchlist",searchlist)
    g.search["searchlist"] = searchlist
    return render_template('order/search_order.html',search_result_form=search_result_form)

@bp.route("/acc_order/<int:OID>",methods=["POST"])
@login_required
def acc_order(OID):
    if acc_order_ID(OID,session['user_uid']) is True:
        return redirect(url_for("user.userinfo"))
    else:
        flash("Error! Others have already accepted this order!")# 前端无法正确显示flash中的内容
        return "Error! Others have already accepted this order!"

@bp.route("/history_order",methods=["GET"])
@login_required
def history_order():
    g.history = {}
    historylist_created=[]
    for OID in return_ordererID_OID(session['user_uid']):
        historylist_created.append((OID,getFormData(OID[0])))
    g.history["historylist_created"] = historylist_created
    historylist_accepted=[]
    for OID in return_ordereeID_OID(session['user_uid']):
        historylist_accepted.append((OID,getFormData(OID[0])))
    g.history["historylist_accepted"] = historylist_accepted
    return render_template('order/history_order.html')