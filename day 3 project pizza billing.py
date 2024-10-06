#in these project i learn conditional statements and Logical operators 

print("Welcome to Python Pizza Deliveries ! ")
bill=0
s=15
m=20
l=25
size=input("what size pizza do you want ? s,m,l : ")
if size=="s":
    bill=15
elif size=="m":
    bill=20
    bill=25
else:
    bill=25
peon=input("do you want pepperonion on it ? y or n: ")
y=2
n=0
if peon=="y":
    bill=bill+2
else:
    bill=bill+0
extracheese=input("do you want extra chesse on iy? y or n: ")
y=3
n=0
if extracheese=="y":
    bill=bill+3
else:
    bill=bill+0   
print("Your final bill is = ",bill)