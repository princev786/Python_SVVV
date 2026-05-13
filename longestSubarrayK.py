#1,2,3,-2,5 k=5
#{1:0,3:1,6:2,4:3,9:4}
lst=eval(input())
k = int(input())
sum,max =0,0
dict = {}

for i in range(len(lst)):
    sum += lst[i]
    if dict.get(sum-k)!=None:
        l = i-dict.get(sum-k)
        if max<l:
            max =l
    
    dict[sum]=i

print(max)

#1 1 1
k=2
{1:1,2:1,}

