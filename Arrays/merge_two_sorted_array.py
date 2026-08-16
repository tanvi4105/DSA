arr1=[-5, -2, 4, 5, 0, 0, 0]
arr2 = [-3, 1, 8]
m=4
n=3

def merge(arr1,m,arr2,n):
    i=m-1
    j=n-1
    k=m+n-1

    while i >= 0 and j >= 0:
        if arr2[j]>arr1[i]:
            arr1[k]=arr2[j]    
            j-=1
        else:
            arr1[k]=arr1[i] 
            i-=1 
        k-=1 

           
    while j>=0:
        if arr2[j]>arr1[i]:
            arr1[k]=arr2[j]    
            j-=1
            k-=1
    return arr1
print(merge(arr1,m,arr2,n))

       

