from wtforms.fields import simple, core
from wtforms import Form, validators, widgets, ValidationError
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
class InfoModifyForm:
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")]
    )
    sex = simple.StringField(
        label='Sex',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Sex can not be empty")]
    )
    QQID = simple.StringField(
        label='QQID',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="QQID can not be empty")]
    )
    WechatID = simple.StringField(
        label='WechatID',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="WechatID can not be empty")]
    )
    phoneNumber = simple.StringField(
        label='PhoneNumber',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="PhoneNumber can not be empty")]
    )
    submit = simple.SubmitField(
        label='Confirm',
        widget=widgets.SubmitInput()
    )