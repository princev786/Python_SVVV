lst = eval(input("Enter list :"))
ele = int(input("Enter  no."))

for i in range(len(lst)-1,-1,-1):
    if lst[i]==ele:
        lst.pop(i)

print(lst)
    
