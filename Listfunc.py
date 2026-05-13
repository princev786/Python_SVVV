lst = [20,10]
lst.append(30) #adds at end
lst.insert(2,25) #adds at spec index
# lst.append([40,50,60])
lst.extend([40,50,60]) # extends the collections in list
# lst.pop(2) # deletes the specified index
# del lst[0:2]
# lst.remove(40)
# lst.clear()

lst.sort(reverse=True) #sort method
lst2 = [5,2,1,7,9,8]
lst3 = sorted(lst2,reverse=True)
# print(lst2)
# print(lst3)

lst4=[1,2,3]
print(lst4*2)
