balance = int(input("Balance :"))
withdraw = int(input("Withdraw :"))

if withdraw > (balance -1000):
    print("Transaction Failed :Minimum balnace voilation")