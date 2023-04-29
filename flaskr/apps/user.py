# from flask import Blueprint
# from flask import flash
# from flask import g
# from flask import redirect
# from flask import render_template
# from flask import request
# from flask import url_for
# from werkzeug.exceptions import abort

# from flaskr.apps.auth import login_required
# from flaskr.db import get_db

# bp = Blueprint("user", __name__,url_prefix="/user")




# def get_user_info(uid):
#     """Get the user's information by id.
    
#     Checks that the id exists and the current user is the uid.
#     If the current user is not the uid, only return the public information.
#     Otherwise, return the public and the private information.
#     Args:
#         uid (int): user's uid

#     Returns:
#         dictionary: the information of the user
#     """
# # Table userInfo:
# # +-------------+--------------+------+-----+---------+----------------+
# # | Field       | Type         | Null | Key | Default | Extra          |
# # +-------------+--------------+------+-----+---------+----------------+
# # | UserInfoID  | int unsigned | NO   | PRI | NULL    | auto_increment |
# # | avatarUrl   | varchar(200) | YES  |     | NULL    |                |
# # | userName    | varchar(45)  | NO   |     | NULL    |                |
# # | sex         | varchar(7)   | YES  |     | NULL    |                |
# # | QQID        | varchar(15)  | YES  |     | NULL    |                |
# # | WechatID    | varchar(20)  | YES  |     | NULL    |                |
# # | phoneNumber | varchar(15)  | YES  |     | NULL    |                |
# # | chuanCoins  | int unsigned | YES  |     | 0       |                |
# # | review      | int unsigned | YES  |     | 0       |                |
# # | UID         | int unsigned | NO   | MUL | NULL    |                |
# # +-------------+--------------+------+-----+---------+----------------+
#     db = get_db()
#     db.execute("SELECT * FROM userInfo WHERE UID = \"{}\"".format(uid))
#     result = db.fetchone()# (UserInfoID, avatorUrl, username, sex, QQID, WechatID, phoneNumber, chuanCoins, review, UID)
#     userinfo=None
#     if result is None:
#         abort(404, f"User id {uid} doesn't exist.")
#     if result[9] != g.user["uid"]:
#         # only return the public informations
#         userinfo={
#             "avatarUrl": result[1],
#             "userName": result[2],
#             "sex": result[3],
#             "QQID": result[4],
#             "WechatID": result[5],
#             "phoneNumber": result[6]
#         }
#     else:
#         userinfo={
#             "avatarUrl": result[1],
#             "userName": result[2],
#             "sex": result[3],
#             "QQID": result[4],
#             "WechatID": result[5],
#             "phoneNumber": result[6],
#             "chuanCoins": result[7],
#             "review": result[8],
#             "UID": result[9]
#         }
#     return userinfo


# @bp.route("/<int:uid>/info")
# def user_info(uid):
#     """Get the user's information by id.
    
#     Checks that the id exists and the current user is the uid.
#     If the current user is not the uid, only return the public information.
#     Otherwise, return the public and the private information.
#     Args:
#         uid (int): user's uid

#     Returns:
#         dictionary: the information of the user
#     """
#     userinfo = get_user_info(uid)
#     # TBD
#     return render_template("user/user_info.html", userinfo=userinfo)
