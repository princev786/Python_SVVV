no_of_hours = float(input("Hours Spend :"))
bill = 0

if no_of_hours<=2:
    bill = no_of_hours*100
elif no_of_hours<=5:
    bill = 2* 100+(no_of_hours-2)*50
else:
    bill = 2*100 + 3*50 + (no_of_hours-5)*25

print("total bill : ",bill)
