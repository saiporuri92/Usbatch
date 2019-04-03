import socket
s=socket.socket()
hostname=socket.gethostname()
port=1025
try:
	s.bind((hostname,port))
	s.listen(32)
	while True:
		print("service running in %s:%s"%(hostname,port))
		cs,ci = s.accept()
		cs.send(b"hello .. connected")
		req_data = cs.recv(1024)
		resp = b"It has digits only" if req_data.isdigit() else b"it contains alphabets also"
		cs.send(resp)
except Exception as err:
	print(err)
finally:
	s.close()