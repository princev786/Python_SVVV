avail = 0
seats = int(input("Seats Required :"))
vip = input("Enter VIP status(yes/no) : ")

if vip=="yes" or seats<=avail:
    print("ticket Confirmed")
else:
    print("Waiting...")