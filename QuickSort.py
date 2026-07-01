def quicksort(lst,p,r):
    if p<r:
        pidx = partition(lst,p,r)
        quicksort(lst,p,pidx-1)
        quicksort(lst,pidx+1,r)

def partition(lst,p,r):
    pivot = lst[r]
    i=p-1
    for curr in range(p,r):
        if lst[curr]<pivot:
            temp = lst[i+1]
            lst[i+1]=lst[curr]
            lst[curr] = temp
            i+=1

    temp = lst[i+1]
    lst[i+1] = lst[r]
    lst[r] = temp
    return i+1

lst=[5,7,2,8,21,4,36,92,45]
quicksort(lst,0,len(lst)-1)
print(lst)
    


        
