# import required modules
# Есть на GIT https://github.com/Dayzpd/Python-Windscribe
import os
from time import sleep
import random

# list of VPN server codes
# codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
#             "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
codeList = ["FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]


try:

    # connect to VPN
    print("1")
    os.system("windscribe connect") #L_9613150717 P_Pr*75
    print("2")
    while True:
        # assigning a random VPN server code
        print("3")
        choiceCode = random.choice(codeList)
        print(f"4 {choiceCode}")

        # changing IP after a particular time period
        sleep(random.randrange(120, 300))
        print("5")

        # connecting to a different VPN server
        print("!!! Changing the IP Address........")
        os.system("windscribe connect " + choiceCode)

except:

    # disconnect VPN
    os.system("windscribe disconnect")
    print("sorry, some error has occurred..!!")