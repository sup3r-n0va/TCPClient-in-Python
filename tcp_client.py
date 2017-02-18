#!/bin/python2

import socket

target_host ="www.google.com"
target_port = 80

#create a socket object
#AF_INET parameter is saying we are going to use a standard IPv4 address
# SOCK_STREAM means that this will be a TCP client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client
client.connect((target_host, target_port))

#send some data
client .send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve some data
response = client.recv(4096)

print response


