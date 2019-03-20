from db_structure import get_conn

def browse_customer():
	con,cur=get_conn()
	cur.execute("select * from customer")
	con.close()
def insert_cutstomer():
	pass