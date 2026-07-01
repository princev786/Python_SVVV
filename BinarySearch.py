def binarysearch(lst,key):
    l = 0
    r = len(lst)-1
    while l <=r:
        mid = l+(r-l)//2
        if lst[mid]==key:
            print(mid+1)
            return
        elif lst[mid]<key:
            l = mid+1
        else:
            r = mid-1
    print(-1)
    
lst = [10,20,30,40,50,60]
key = int(input())
binarysearch(lst,key)


    