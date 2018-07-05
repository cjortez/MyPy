tax=1.08
tip=1.18
meal=input("How much was the food?")
meal=float(meal)
cost_of_meal=[tax, tip]

subtotal=meal*tax
totalcost=subtotal*tip

print(totalcost)