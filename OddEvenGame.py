num = int(input("Enter a No. :"))
even,odd = 0,0 
while(num):
    if num%2==0:
        even += 1
    else:
        odd += 1
    
    num = int(input("Enter No. :"))

print("Even Count ",even)
print("Odd Count ",odd)
