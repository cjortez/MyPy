
dull=.10
prim=.25

Bottles=input().split(",")

counter=0
for dulla in Bottles:
    if float(dulla) < 1:
        counter+=1
        
print("Small Bottles: ", counter)

counter_one=0        
for prime in Bottles:
    if float(prime) >= 1:
        counter_one+=1

print("Big Bottles: ", counter_one)

total=("Refund $", ((counter_one*prim)+(counter*dull)))

print(total)

