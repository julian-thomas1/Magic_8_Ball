#Modules
import random
import time
import os

#Functions
def shakeBall(): #Shakes an ascii 8 ball on the screen.
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
	#Ask - What question does the user have?
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
	while userQuestion=="": #Make sure there is a question. If the user typed nothing, loop back and ask again.
		userQuestion=input("")
		if userQuestion == "": print("That's not a question!")
	os.system('cls') #clear screen
	
	
	

	#Contemplating - simulate thinking.
	responses=open("ProgramData/responses.txt",'r').read().splitlines() #Load responses from ProgramData/responses.txt
	shakeBall()




	#Answer - provide user with a random answer.
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
	print(responses[random.randint(0,29)]) #Pick a random response from the file loaded during the 'Contemplating' phase.
	input("\n\nPress ENTER to ask another question!")
	os.system('cls') #clear screen
