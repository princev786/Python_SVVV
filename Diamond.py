n = 4

for i in range(1,2*n):
    if i<=n:
        for k in range(1,n-i+1):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
    else:
        for k in range(1,i-n+1):
            print(" ",end="")
        for j in range(1,2*(2*n-i)):
            print("*",end="")
    print()