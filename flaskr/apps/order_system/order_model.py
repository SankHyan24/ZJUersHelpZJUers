from flaskr.db import get_db
from flaskr.apps.order_system.order_form import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# Table user:
# +-------------+--------------+------+-----+---------+----------------+
# | Field       | Type         | Null | Key | Default | Extra          |
# +-------------+--------------+------+-----+---------+----------------+
# | UID         | int unsigned | NO   | PRI |    -    | auto_increment |
# | Password    | varchar(103) | NO   |     |    -    |                |
# | email       | varchar(60)  | NO   |     |    -    |                |
# +-------------+--------------+------+-----+---------+----------------+

# Table userInfo:
# +-------------+--------------+------+-----+---------+----------------+
# | Field       | Type         | Null | Key | Default | Extra          |
# +-------------+--------------+------+-----+---------+----------------+
# | UserInfoID  | int unsigned | NO   | PRI | NULL    | auto_increment |
# | avatarUrl   | varchar(200) | YES  |     | NULL    |                |
# | userName    | varchar(45)  | NO   |     | NULL    |                |
# | sex         | varchar(7)   | YES  |     | NULL    |                |
# | QQID        | varchar(15)  | YES  |     | NULL    |                |
# | WechatID    | varchar(20)  | YES  |     | NULL    |                |
# | phoneNumber | varchar(15)  | YES  |     | NULL    |                |
# | chuanCoins  | int unsigned | YES  |     | 0       |                |
# | review      | int unsigned | YES  |     | 0       |                |
# | UID         | int unsigned | NO   | MUL | NULL    |                |
# +-------------+--------------+------+-----+---------+----------------+

# def infoModify(user_id:int, data:[]):
#     db = get_db()

#     if data['userName']:
#         update = "update userInfo SET userName = \'" + str(data['userName']) + "\' where UID = \'" + user_id + '\''
#         db.execute(update)
#         db.connection.commit()
#     if data['sex']:
#         update = "update userInfo SET sex = \'" + str(data['sex']) + "\' where UID = \'" + user_id + '\''
#         db.execute(update)
#         db.connection.commit()
#     if data['QQID']:
#         update = "update userInfo SET QQID = \'" + str(data['QQID']) + "\' where UID = \'" + user_id + '\''
#         db.execute(update)
#         db.connection.commit()
#     if data['WechatID']:
#         update = "update userInfo SET WechatID = \'" + str(data['WechatID']) + "\' where UID = \'" + user_id + '\''
#         db.execute(update)
#         db.connection.commit()
#     if data['phoneNumber']:
#         update = "update userInfo SET phoneNumber = \'" + str(data['phoneNumber']) + "\' where UID = \'" + user_id + '\''
#         db.execute(update)
#         db.connection.commit()


# def info_register(data:[]):
#     db = get_db()
#     email = data['email']
#     pwd = generate_password_hash(data["password"])
#     query = "insert into user (email, password) values (\"{}\",\"{}\")".format(email,pwd)
#     query2 = "select * from user where email=\"{}\"".format(email)
#     try:
#         db.execute(query)
#         db.connection.commit()
#     except db.IntegrityError:
#         # The email was already taken, which caused the
#         # commit to fail. Show a validation error.
#         error = f"EMAIL: {email} is already registered."
#         flash(error)

#     db.execute(query2)
#     result=db.fetchone()

#     uid, pwd, email = result
#     query3 = "insert into userInfo VALUES (null, null, \"{}\",\"{}\",\"{}\",\"{}\")".format\
#         (data['username'],data['sex'],data['QQID'],data['WechatID'],data['phoneNumber'])
    
#     try:
#         db.execute(query3)
#         db.connection.commit()
#     except db.IntegrityError:
#         # The email was already taken, which caused the
#         # commit to fail. Show a validation error.
#         error = f"EMAIL: {email} is already registered."
#         flash(error)
   

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

def return_newest_ID():
    query = "SELECT OID FROM orderInfo ORDER BY startTime LIMIT 20"
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
    query = "SELECT startTime, dueTime, remark, location, moneyNum, chuanCoinsNum FROM orderInfo WHERE OID =" + str(OID)
    db = get_db()
    try:
        db.execute(query)
        db.connection.commit()
        formdata = db.fetchone()
        retForm = OrderInfoForm(formdata)
        return OID
    except db.IntegrityError:
        error = f"Get form orders failed."
        flash(error)
    
