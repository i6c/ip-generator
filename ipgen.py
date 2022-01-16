import random
import socket
import struct
import time

print("Starting Engine!")
time.sleep(1)
print("\n")
print("██╗██████╗░  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
print("██║██╔══██╗  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("██║██████╔╝  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
print("██║██╔═══╝░  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
print("██║██║░░░░░  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
print("╚═╝╚═╝░░░░░  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
print("Developed By: @Drexy2")
print("Join TG: @FreeHQCombo")
print("\n")
time.sleep(1)
print("Use with caution. You are responsible for your actions")
print("I have no liability and am not responsible for any misuse or legal damage from your actions.")
print("\n")

number = int(input('How much IPs do you want to generate?: '))
print("Results saved to IPResult.txt!")
saveresultt = open('IPResult.txt', 'w')


for _ in range(number):
    print(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))), file = saveresultt)
