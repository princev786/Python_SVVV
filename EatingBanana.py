def isFeasible(lst,h,s):
    sum=0
    for p in lst:
        sum += (p+s-1)//s

    return sum<=h

lst = [1,5,8,9,11]
h=8

min = 1
max = 11
s=0
while min<=max:
    s = min +(max-min)//2
    if(isFeasible(lst,h,s)):
        max = s-1
    else:
        min = s+1

print(min)
