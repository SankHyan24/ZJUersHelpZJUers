from dotenv import load_dotenv
import pymysql
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from util.mysql import get_db_info

hasrun=False
if not hasrun:
    load_dotenv()

from flask import g,Flask,current_app

def get_db():
    if 'db' not in g:
        db_info=get_db_info()
        g.db = pymysql.connect(
            host=db_info['host'],
            database=db_info['database'],
            user=db_info['user'],
            password=db_info['password'],
            ssl_ca=os.getenv("SSL_CERT")
        ).cursor()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
def init_db(app:Flask):
    app.teardown_appcontext(close_db)

# These code only run for testing
if __name__ == '__main__':      
    db_info=get_db_info()
    conn=pymysql.connect(
                host=db_info['host'],
                database=db_info['database'],
                user=db_info['user'],
                password=db_info['password'],
                ssl_ca=os.getenv("SSL_CERT")
            )
    cursor = conn.cursor()
    cursor.execute("select @@version ")
    version = cursor.fetchone()
    if version:
        print('Running version: ', version)
    else:
        print('Not connected.')
    conn.close()