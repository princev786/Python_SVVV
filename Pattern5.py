n =5
num =65
for i in range(1,n+1):

    if i%2==0:
        print(chr(num+1),end="")
        print(chr(num),end="")
        print(chr(num+2),end="")
        num+=3
    else:
        print(" ",end="")
        print(chr(num),end="")
        num+=1
        
    print()