import mysql.connector as dbapi
import datetime
conn = dbapi.Connect(host='127.0.0.1', port='3306',
                     user='root', database='test')
cur = conn.cursor()


def database_call(comp_id):
    try:
        cur.execute(f'SELECT * from comp_info where id = {comp_id}')
        comp_data = cur.fetchall()
        cur.execute(
            "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='test' AND TABLE_NAME='comp_info';")
        key_raw = cur.fetchall()
        key = []
        for k in key_raw:
            key.append(k[0])
        data_list = zip(key, list(comp_data[0]))
        dict = {}
        for k, v in data_list:
            dict[k] = v

        return dict
    except:
        return "Not in Database"


def logger(ip, comp_id):
    date = datetime.datetime.now()
    cur.execute('insert into request_log values("%s","%s","%s");' % (date, ip, comp_id))
    conn.commit()
