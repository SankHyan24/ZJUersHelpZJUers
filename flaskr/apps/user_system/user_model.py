from flaskr.db import get_db

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

def info_modify(user_id:int, data:[]):
    db = get_db()

    if data['userName']:
        update = "update userInfo SET userName = \'" + str(data['userName']) + "\' where UID = \'" + user_id + '\''
        db.execute(update)
        db.connection.commit()
    if data['sex']:
        update = "update userInfo SET sex = \'" + str(data['sex']) + "\' where UID = \'" + user_id + '\''
        cursor.execute(update)
        db.connection.commit()
    if data['QQID']:
        update = "update userInfo SET QQID = \'" + str(data['QQID']) + "\' where UID = \'" + user_id + '\''
        cursor.execute(update)
        db.connection.commit()
    if data['WechatID']:
        update = "update userInfo SET WechatID = \'" + str(data['WechatID']) + "\' where UID = \'" + user_id + '\''
        cursor.execute(update)
        db.connection.commit()
    if data['phoneNumber']:
        update = "update userInfo SET phoneNumber = \'" + str(data['phoneNumber']) + "\' where UID = \'" + user_id + '\''
        cursor.execute(update)
        db.connection.commit()