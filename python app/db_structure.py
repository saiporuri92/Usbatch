# create table queries
import psycopg2
import json
f=open("config.json")
config_data = json.load(f)
def get_conn():
	con = psycopg2.connect(**config_data)
    cur=con.cursor()
    return con, cur
if __name__ == "__main__":
	con,cur=get_conn()
	q="create table customer (id int, name varchar(250))"
	cur.execute(q)
	con.close()