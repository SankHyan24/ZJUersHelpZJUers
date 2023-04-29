from flaskr.db import get_db


def get_search_result(search_term):
    db = get_db()
    query = "SELECT * FROM orderInfo WHERE remark LIKE \'%{}%\'".format(search_term)
    # print(query)
    db.execute(query)
    db.connection.commit()
    return db.fetchall()