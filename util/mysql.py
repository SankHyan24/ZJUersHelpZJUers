import json
import os
import sys

# get the DataBase URI from the json file
def get_db_info():
    with open(os.path.join(os.path.dirname(__file__), '../opt/mysql.json')) as f:
        json_data = json.load(f)
        db_host=json_data['host']
        db_port=json_data['port']
        db_user=json_data['user']
        db_passwd=json_data['passwd']
        db_usedb=json_data['usedb']
    # db_URI=f"mysql+pymysql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_usedb}"
    return {'host':db_host,'port':db_port,'user':db_user,'password':db_passwd,'database':db_usedb}
