Pull=input()

alpha=0
digit=0
space=0

for strings in Pull:
	if strings.isalpha():
		alpha+=1
	elif strings.isdigit():
		digit+=1 
	elif strings == " ":
		space+=1
		
print(alpha, digit, space)
