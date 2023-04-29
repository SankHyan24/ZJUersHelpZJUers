from flaskr.db import get_db


def findstrinreq(search_term):
    db = get_db()
    query = "SELECT * FROM orderInfo WHERE column LIKE ?", ('%' + search_term + '%',)
    db.execute(query)
    db.connection.commit()
    return db.fetchall()