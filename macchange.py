import os
import re
import subprocess
from random import choice, randint


def change_mac(inter, add):
    subprocess.call(["ifconfig " + str(inter) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(inter) + " hw ether " + str(add)], shell=True)
    subprocess.call(["ifconfig " + str(inter) + " up"], shell=True)


def mac_random():
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])

    for i in range(3):
        byte1 = str((randint(0, 9)))
        byte2 = str((randint(0, 9)))
        num = str(byte1 + byte2)

        mac_address.append(num)
        return ":".join(mac_address)


def current_mac():
    output = subprocess.check_output(["ifconfig " + "wlan0"], shell=True)
    curr_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    str(curr_mac)
    print("Your current mac address is " + curr_mac[0])


def in_sudo_mode():
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()


print(colored(figlet_format("mac changer", font="pagga"), color="blue"))


in_sudo_mode()

interface = input("ENTER YOUR INTERFACE NAME: ").strip()

print("""
1. Assign a mac address
2. Create a random mac address
3. View current mac address
4. Exit
""")
option = input("Pick an operation:")
match option:
    case "1":
        mac = input("ENTER THE NEW MAC ADDRESS:")
        change_mac(interface, mac)
    case "2":
        random_mac = mac_random()
        change_mac(interface, random_mac)
    case "3":
        current_mac()
    case "4":
        exit(0)
    case _:
        print("invalid choice!")
