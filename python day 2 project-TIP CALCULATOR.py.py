#python day 2 project "TIP CALCULATOR"
#topics covered  python : primitive data types,type error, type checking,
#type conversion ,mathematical operators in python,number manipulation 
#and F string in python


print("Welcome to the tip calculator !")
print("what was the total bill ?")
bill=int(input("$"))
print("How much tip would you like to give ? 0,10,15,or your wish ?")
tip=int(input("$"))
print("How many people to split the bill ? ")
split=int(input( " "))
if tip!= 0:
    per_person=(bill+tip)/split
else:
     per_person=bill/split
print("Each person should pay : $",per_person)
