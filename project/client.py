import requests
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