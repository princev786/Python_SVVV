no_of_units = int(input("Enter No. of Units"))
bill =50

if no_of_units<=100:
    bill += no_of_units *1.5
elif no_of_units<=200:
    bill += 100 *1.5 + (no_of_units-100)*3.5
else:
    bill += 100*1.5 + 100*3.5 +(no_of_units-200)*5

if bill>2000:
    bill = bill * 1.1

print("Total Bill :",bill)
