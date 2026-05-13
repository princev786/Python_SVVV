#Fixed sliding window
lst = eval(input())
max,count=0,0

for i in lst:
    if i==0:
        count+=1
    else:
        if count>max :
            max = count
        count =0
if count>max:
    max = count

print(max)
