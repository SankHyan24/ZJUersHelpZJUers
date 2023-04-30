from flaskr.db import get_db
from flaskr.apps.order_system.order_form import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#  describe orderInfo;
# +---------------+-----------------------+------+-----+---------+----------------+
# | Field         | Type                  | Null | Key | Default | Extra          |
# +---------------+-----------------------+------+-----+---------+----------------+
# | OID           | int unsigned          | NO   | PRI | NULL    | auto_increment |
# | startTime     | datetime              | NO   |     | NULL    |                |
# | dueTime       | datetime              | NO   |     | NULL    |                |
# | remark        | varchar(400)          | YES  |     | NULL    |                |
# | location      | varchar(80)           | NO   |     | NULL    |                |
# | moneyNum      | decimal(9,2) unsigned | NO   |     | 0.00    |                |
# | chuanCoinsNum | int unsigned          | NO   |     | 0       |                |
# | orderState    | int unsigned          | YES  |     | NULL    |                |
# | ordererID     | int unsigned          | NO   | MUL | NULL    |                |
# | ordereeID     | int unsigned          | YES  | MUL | NULL    |                |
# +---------------+-----------------------+------+-----+---------+----------------+

def order_create(user_id:int, data): # TODO test
    db = get_db()
    startTime = data['startTime']
    dueTime = data['dueTime']
    remark = data['remark']
    location = data['location']
    moneyNum = data['moneyNum']
    chuanCoinsNum = data['chuanCoinsNum']
    
    
    query = "insert into orderInfo (startTime, dueTime, remark, location, moneyNum, chuanCoinsNum, ordererID)  VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format\
        (startTime,dueTime,remark,location,moneyNum,chuanCoinsNum,user_id)
    
    
    try:
        db.execute(query)
        db.connection.commit()
    except db.IntegrityError:

        error = f"Order create failed."
        flash(error)

def return_latest_ID(pageNumber:int):
    query = "SELECT OID FROM orderInfo ORDER BY startTime DESC LIMIT 20 OFFSET " + str((pageNumber-1) * 20)
    db = get_db()
    try:
        db.execute(query)
        db.connection.commit()
        OID = db.fetchall()
        return OID
    except db.IntegrityError:
        error = f"Get new orders failed."
        flash(error)

def getFormData(OID:int):
    query = "SELECT startTime, dueTime, remark, location, moneyNum, chuanCoinsNum, ordererID, orderState FROM orderInfo WHERE OID = " + str(OID)
    db = get_db()
    try:
        db.execute(query)
        # db.connection.commit()
        formdata = db.fetchone()
        return formdata
    except db.IntegrityError:
        error = f"Get form orders failed."
        flash(error)
        
def acc_order_ID(OID:int, user_id:int):
    db=get_db()
    flash("acc_order_ID")
    # first check the ordererID is not the same as user_id
    query1 = "SELECT ordererID,orderState FROM orderInfo WHERE OID = " + str(OID)
    try:
        db.execute(query1)
        res = db.fetchone()
        ordererID = res[0]
        orderState = res[1]
        print("ordererID: ", ordererID)
        print("user_id: ", user_id)
    except db.IntegrityError:
        error = f"Get ordererID failed."
        flash(error)
    if ordererID == user_id:
        flash("You can't accept your own order!")
        return False
    if orderState == 1:
        flash("This order has been accepted!")
        return False
    # set the ordereeID as user_id
    query2 = "UPDATE orderInfo SET ordereeID = " + str(user_id) + ", orderState = 1 " + "WHERE OID = " + str(OID)
    try:
        db.execute(query2)
        db.connection.commit()
    except db.IntegrityError:
        error = f"Accept order failed."
        flash(error)
        return False
    return True
    
    
def return_ordererID_OID(user_id:int):
    query = "SELECT OID FROM orderInfo where ordererID = " + str(user_id)
    db = get_db()
    print(query)
    try:
        db.execute(query)
        OID = db.fetchall()
        return OID
    except db.IntegrityError:
        error = f"Get orders failed."
        flash(error)
        
def return_ordereeID_OID(user_id:int):
    query = "SELECT OID FROM orderInfo where ordereeID = " + str(user_id) + " AND orderState = 1"
    db = get_db()
    print(query)
    try:
        db.execute(query)
        OID = db.fetchall()
        return OID
    except db.IntegrityError:
        error = f"Get orders failed."
        flash(error)

def changeOrderState(OID,state):
    query = "UPDATE orderInfo SET orderState = " + str(state) + " WHERE OID = " + str(OID)
    db = get_db()
    try:
        db.execute(query)
        db.connection.commit()
    except db.IntegiryError:
        error = f"Change orderstate failed."
        flash(error)
