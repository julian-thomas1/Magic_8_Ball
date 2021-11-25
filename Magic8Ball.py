#Modules
import random
import time
import os

#Functions
def shakeBall():
    i=0
    while i<5:
        print("         _......._")
        print("      .-:::::::::::-.")
        print("    .:::::::::::::::::.")
        print("   :::::::' .-. `:::::::")
        print("  :::::::  :   :  :::::::")
        print(" ::::::::  :   :  ::::::::")
        print(" :::::::::._`-'_.:::::::::")
        print(" :::::::::' .-. `:::::::::")
        print(" ::::::::  :   :  ::::::::")
        print("  :::::::  :   :  :::::::")
        print("   :::::::._`-'_.:::::::")
        print("    `:::::::::::::::::'")
        print("      `-:::::::::::-'")
        print("         `'''''''`")
        time.sleep(0.1)
        os.system('cls') #clear screen
        print("             _......._")
        print("          .-:::::::::::-.")
        print("        .:::::::::::::::::.")
        print("       :::::::' .-. `:::::::")
        print("      :::::::  :   :  :::::::")
        print("     ::::::::  :   :  ::::::::")
        print("     :::::::::._`-'_.:::::::::")
        print("     :::::::::' .-. `:::::::::")
        print("     ::::::::  :   :  ::::::::")
        print("      :::::::  :   :  :::::::")
        print("       :::::::._`-'_.:::::::")
        print("        `:::::::::::::::::'")
        print("          `-:::::::::::-'")
        print("             `'''''''`")
        time.sleep(0.1)
        os.system('cls') #clear screen
        i+=1

#Main
while True:
	#Ask
	print("           _......._")
	print("        .-:::::::::::-.")
	print("      .:::::::::::::::::.")
	print("     :::::::' .-. `:::::::")
	print("    :::::::  :   :  :::::::")
	print("   ::::::::  :   :  ::::::::")
	print("   :::::::::._`-'_.:::::::::")
	print("   :::::::::' .-. `:::::::::")
	print("   ::::::::  :   :  ::::::::")
	print("    :::::::  :   :  :::::::")
	print("     :::::::._`-'_.:::::::")
	print("      `:::::::::::::::::'")
	print("        `-:::::::::::-'")
	print("           `'''''''`")
	print("\n")



	print("Ask the Magic 8Ball a question!")
	
	userQuestion=""
	while userQuestion=="":
		userQuestion=input("")
		if userQuestion == "": print("That's not a question!")
	os.system('cls') #clear screen

	#Contemplating
	responses=open("data/responses.txt",'r').read().splitlines()
	shakeBall()

	#Answer
	print("           _......._")
	print("        .-:::::::::::-.")
	print("      .:::::::::::::::::.")
	print("     :::::::' .-. `:::::::")
	print("    :::::::  :   :  :::::::")
	print("   ::::::::  :   :  ::::::::")
	print("   :::::::::._`-'_.:::::::::")
	print("   :::::::::' .-. `:::::::::")
	print("   ::::::::  :   :  ::::::::")
	print("    :::::::  :   :  :::::::")
	print("     :::::::._`-'_.:::::::")
	print("      `:::::::::::::::::'")
	print("        `-:::::::::::-'")
	print("           `'''''''`")
	print("")
	print(userQuestion)
	print("\nThe Magic 8Ball SAYS...\n")
	time.sleep(1)
	print(responses[random.randint(0,29)])
	input("\n\nPress ENTER to ask another question!")
	os.system('cls') #clear screen
