import socket
s=socket.socket()
try:
	s.connect(("GSSHYD-CP-LT6973",1025))
	ack=s.recv(1024)
	print(ack)
	s.send(b"12sdfsf")
	resp=s.recv(1024)
	print(resp)
except Exception as err:
	print(err)
finally:
	s.close()