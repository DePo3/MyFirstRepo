def sound (volume): 
	if volume < 20:
		print("It is quiet.")
	elif volume < 30:
		print("It is a good background.")
	else: 
		print("It is too loud.")

sound(18)
sound(22)
sound(27)
