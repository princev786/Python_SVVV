#length of longest substring having at most K distinct characters
str = input()
k = int(input())
dict={}
l=0
max =0

for i in range(len(str)):
    if str[i] not in dict:
        dict[str[i]]=1
    else:
        dict[str[i]]+=1

    if len(dict.keys())<=k and max<i-l+1:
        max = i-l+1

    while len(dict.keys())>k:
        dict[str[l]]-=1
        if dict[str[l]]==0:
            del dict[str[l]]    
        l+=1

print(max)
    
