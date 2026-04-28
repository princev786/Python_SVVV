amt = int(input("Enter Amount :"))
premium = input("Premium Membership(yes/no) :")

if amt>=5000:
    amt = amt *0.8
elif amt>=3000:
    amt = amt * 0.9

if premium == "yes":
        amt = amt * 0.95

print("Total Bill : ",amt)  