import socket

#create socket connection
c = socket.socket()
c.connect(('192.168.0.10',10940))

#send/receive through socket
sent_bytes = c.send(b'000EAR00A012\n')
output,addr = c.recvfrom(5000)
val = str(output.decode('ascii'))

#Assigning error codes to variables
error_status = val[14]
error_code = val[15:17]

#print values
if error_status == '1':
    print('Error status: Detected')
else:
    print('Error status: Not detected')
    
if error_code =='00':
    print('Error code: Nil')
else:
    print('Error code:', (int(error_code)+40))
#close socket conneciton
c.close()
