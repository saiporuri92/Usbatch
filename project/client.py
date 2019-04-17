import requests
'''
#url="http://localhost:8000/airports/"
# resp=requests.post(url,json={"name":"vijayawada","lat":"234","log":"45678"})
# print(resp.json())
url="http://localhost:8000/airports/5/"
# resp=requests.put(url,data={"lat":"234567","log":"26789456"})
# print(resp.json())
resp=requests.delete(url)
# print(resp.json())
resp=requests.get(url)
print(resp.json())

url="http://localhost:8000/airports/"
resp=requests.post(url,json={"name":"vijayawada","lat":"234","log":"45678"}, 
	auth=("samba","samba1234"))
print(resp.json(),resp.status_code)
resp=requests.get(url,auth=("samba","samba1234"))
print(resp.json(),resp.status_code)
'''
'''
url="http://localhost:8000/airports/"
resp=requests.post(url,json={"name":"vijayawada","lat":"234","log":"45678"}, 
	#auth=("samba","samba1234"),
headers={"Authorization":"Token 637e4ccdb530e3d200db1d44dc7159e3260b0fdf"}
	)

print(resp.json(),resp.status_code)
resp=requests.get(url)
print(resp.json(),resp.status_code)
'''
'''
url="http://localhost:8000/airports/"
resp=requests.post(url,json={"name":"vijayawada","lat":"234","log":"45678"}
	)
print(resp,resp.status_code)
'''
url="http://localhost:8000/get_short_path/"
resp=requests.get(url, 
	json={"airports":["begumpet","vizag","shamshabad"],"source":"vizag"})
print(resp.status_code,resp.json())

