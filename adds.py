import pymysql.cursors

def connect():
    connection = pymysql.connect(
        host='remotemysql.com',
        user='VcJhVl8VY9',
        password='2szV2WF4BO',
        db='VcJhVl8VY9',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection