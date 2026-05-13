#find second duplicate
lst = eval(input("Enter list :"))
ele = int(input("Enter  no."))
c =3 #2 1 0
# 1 2 3 4 1 2 15 1
for i in range(len(lst)):
    if lst[i] == ele:
        c-=1

    if c==0:
        print(i)
        break
else:
    print("Not Exist")


