# just a simple calculator that I will keep adding to, to make it more & more sophisticated opinions welcomed!

calcu=input("Function: ",)
x=int(input("x= ",))
y=int(input("y= ",))

def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
def power(x,y):
    print(x**y)
def remain(x,y):
    print(x%y)
def floor(x,y):
	print(x//y)

	if calcu == add:
		print(x+y)
	elif calcu == subtract:
		print(x-y)
	elif calcu == multiply:
		print(x*y)
	elif calcu == divide:
		print(x/y)
	elif calcu == power:
		print(x**y)
	elif calcu == remain:
		print(x%y)
	elif calcu == floor:
		print(x//y)