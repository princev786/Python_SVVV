#find max sum in K size window
lst = eval(input())
k = int(input())
sum,max =0,0

for ele in range(k):
    sum+=lst[ele]
if max<sum:
    max = sum
for i in range(k,len(lst)):
    sum -= lst[i-k]
    sum += lst[i]
    if sum>max:
        max = sum

print(max)

