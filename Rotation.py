lst = eval(input("Enter list :"))
k = int(input("Enter K :"))
#1  2 3 4 5 

for i in range(k):
    item = lst.pop()
    lst.insert(0,item)

print(lst)