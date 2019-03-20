import json
import os
db_name=input("enter db name:")
host=input("enter host:")
port=input("enter post:")
user=input("Enter user:")
password=input("enter password:")
config_data = {"database":db_name,
"host":host,
"port":port,
"user":user,
"password":password}
f=open("config.json","w")
f.dump(config_data,f)
f.close()
os.system("python db_structure.py")

