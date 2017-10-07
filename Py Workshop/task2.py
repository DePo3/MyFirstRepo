print()
print("What is your name?")

name = input("> ")
print()

print("Hello %s, welcome to the dungeion!" % (name))
print("Do you go through door 1, door 2 or door 3?")

def wrong_input(username):
	print("You are not so good with numbers %s, are you?" % (username))

def dead (death_message):
	print("You died.", death_message)

door = input(">")
print()

if door =="1":
	print("%s , there is a nice vampire asking you if you enjoy life." % (name))
	print("What do you do?")
	print("1.Smile and nod.")
	print("2.Scream and run.")

	vampire = input ("> ")
	print()

	if vampire =="1":
		print("Congratulations %s, you found a new friend!" % (name))
	elif vampire =="2":
		dead("Sorry %s, the vampire was faster. You became dinner." % (name))
	else:
		wrong_input (name)

	print()

elif door =="2":
	print ("%s, there is a big werewolf asking for a hug." % (name))
	print ("What do you do?")
	print ("1. Give a hug.")
	print ("2. Scream and run.")

	werewolf = input ("> ")
	print()

	if werewolf =="1":
		print("Congratulations %s, you just had a nice hug with a werewolf!" % (name))
	elif werewolf =="2":
		dead("Sorry %s, the werewolf's feeling got hurt and you became dinner." % (name))
	else:
		wrong_input (name)
	print()

elif door =="3":
	print ("There is an old witch asking if you want to fly on her broom.")
	print("What do you do?")
	print("1.Nod and take the broom.")
	print("2. Scream and run away.")

	witch = input ("> ")
	print()

	if witch =="1":
		dead("You jumped with a broom out of a window. Oops.")
	elif witch =="2":
		print("Congratulations!You managed to run away from an old woman.")
	else:
		wrong_input (name)
	print()

else:
	wrong_input (name)
