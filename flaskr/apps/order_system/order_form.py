from wtforms.fields import simple, core
from wtforms import Form, validators, widgets, ValidationError
# Table orderInfo:
#+---------------+-----------------------+------+-----+---------+-------+
#| Field         | Type                  | Null | Key | Default | Extra |
#+---------------+-----------------------+------+-----+---------+-------+
#| OID           | int unsigned          | NO   | PRI | NULL    |       |
#| startTime     | datetime              | NO   |     | NULL    |       |
#| dueTime       | datetime              | NO   |     | NULL    |       |
#| remark        | varchar(400)          | YES  |     | NULL    |       |
#| location      | varchar(80)           | NO   |     | NULL    |       |
#| moneyNum      | decimal(9,2) unsigned | NO   |     | 0.00    |       |
#| chuanCoinsNum | int unsigned          | NO   |     | 0       |       |
#| orderState    | int unsigned          | NO   |     | NULL    |       |
#| ordererID     | int unsigned          | NO   | MUL | NULL    |       |
#| ordereeID     | int unsigned          | YES  | MUL | NULL    |       |
#+---------------+-----------------------+------+-----+---------+-------+
class OrderInfoForm(Form):
    startTime = simple.DateTimeField(
        label='startTime',
        widget=widgets.DateTimeInput(),
        validators=[validators.DataRequired(message="StartTime can not be empty")]
    )
    dueTime = simple.DateTimeField(
        label='dueTime',
        widget=widgets.DateTimeInput(),
        validators=[validators.DataRequired(message="DueTime can not be empty")]
    )
    remark = simple.StringField(
        label='remark',
        widget=widgets.TextInput()
    )
    location = simple.StringField(
        label='location',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Location can not be empty")]
    )
    moneyNum = simple.IntegerField(
        label='moneyNum',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="MoneyNum can not be empty")]
    )
    chuanCoinsNum = simple.IntegerField(
        label='chuanCoinsNum',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="ChuanCoinsNum can not be empty")]
    )
    submit = simple.SubmitField(
        label='Confirm',
        widget=widgets.SubmitInput()
    )

