#name="mark"
time=input("What time is it")
time=int(time)
print(type(time))
list_of_friends=["Emily", "John", "Mark"]

for name in list_of_friends:
	if time < 7:
		print("Hello", name, "Party starts at 7")
	elif time==7:
		print("Hello", name, "You are right on time")
	else:
		print("Hello", name, "You are late")
