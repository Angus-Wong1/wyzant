from socket import *
import random
import time

#server_ip = '138.26.210.245' 
server_ip = '' 
bid = 'pwp'
localhost = '' 
serverPort = 3310 

# connecting to Robot on port 3310 and sending bid
# make a socket and connect to the robot.py 
s1 = socket(AF_INET, SOCK_STREAM) #init socket
s1.connect((server_ip, serverPort))#connect to robot
bid1 = bid.encode() #encode str to byte
s1.send(bid1)# send to robot

# creating TCP socket s2 at port from recvd port, to accept new connection

port2 = int(s1.recv(100))#recv from robot and cast int

s2 = socket(AF_INET, SOCK_STREAM)
s2.bind((localhost, port2)) #bind

s2.listen(5) #listen for connection from robot
s2, addr = s2.accept()
print("\nClient from %s at port %d connected" %(addr[0],addr[1]))




# decoding the message to create a UDP socket s3 to sent variable num to   port studen
# then recieving the string on port robot

UDP_init = s2.recv(200).decode().split(',') #recv and decode byte and split str at ,
UDPlist = list(map(int, UDP_init)) # enum and cast to list
student_port = UDPlist[0] 
robot_port = UDPlist[1]
s3 = socket(AF_INET,SOCK_DGRAM) 

num = str((random.randint(5,9))).encode()# choose ran num

s3.sendto(num,(server_ip, student_port)) #send 

#('Recieving packets from ROBOT on s3')

s_3 = socket(AF_INET, SOCK_DGRAM)
s_3.bind((localhost, robot_port))

message, serAddr = s_3.recvfrom(2048)
print('Recieved packets from s_3 robot port:' + message.decode())


#  sending back the string to Robot, 5 times, once every second
for i in range(0,5):
    s3.sendto(message,(server_ip, student_port)) #send 
    time.sleep(1)# wait one sec
    print(i+1)

