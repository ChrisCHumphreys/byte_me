#!/usr/bin/python3
# Echo client program
import socket
import time
import re
import sys

# items = ['ab', 'aa', 'aaa', 'aaaaa']

def clean_output(query, response):
    spaces = int(-1 * (len(query) - 10))
    pattern = r'[0-9*a-f*0-9*]{34,}'
    code = re.findall(pattern, str(response))
    try:
        print(str(query + (spaces * ' ') + " : " + code[0] + '\n'))
        return str(query + (spaces * ' ') + " : " + code[0] + '\n')
    except: 
        return str(query + " : error\n")

outfile = open("results.txt", "w")
infile = open(sys.argv[1], "r")

items = infile.read()
items = items.split()

infile.close()

HOST = 'crypto.chal.csaw.io'    # The remote host
PORT = 1003              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(1024)
outfile.write(clean_output('', data))
time.sleep(1)

for item in items:
    s.sendall(str(item + '\n').encode('utf-8'))
    time.sleep(1)
    data = s.recv(1024)
    # print(str(data))
    outfile.write(clean_output(item, data))

s.close()
outfile.close()

