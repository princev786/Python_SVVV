def mergesort(lst,p,r):
    if p<r:
        q = (p+r)//2
        mergesort(lst,p,q)
        mergesort(lst,q+1,r)
        merge(lst,p,q,r)

def merge(lst,p,q,r):
    left = []
    right = []

    for i in range(p,q+1):
        left.append(lst[i])
    for j in range(q+1,r+1):
        right.append(lst[j])
    
    n1 = q-p+1
    n2 = r-q

    i,j,k  = 0,0,p
    while i<n1 and j<n2:
        if left[i]<=right[j]:
            lst[k] = left[i]
            i+=1
        else:
            lst[k] = right[j]
            j+=1
        k+=1
    while i<n1:
        lst[k]=left[i]
        k+=1
        i+=1
    while j<n2:
        lst[k]=right[j]
        k+=1
        j+=1
    


lst = [5,7,2,6,9,3,1]
mergesort(lst,0,len(lst)-1)
print(lst)


