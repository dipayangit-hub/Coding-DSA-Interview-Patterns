def selectionsort(arr:list):
    #choose the minimum element in every iteration and put it at correct place
    for i in range(len(arr)-1):
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        if minindex!=i:
            arr[i],arr[minindex]=arr[minindex],arr[i]

    return arr



def insertionsort(arr:list):
#assume arr[0] is sorted and insert arr[i] into the sorted left position
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        k=i
        while j>=0 and arr[j]>key:
            arr[j],arr[k]=key,arr[j]
            j-=1
            k-=1
    return arr

def mergesort(arr:list,left,right):
    #divide and conquer , then merge---use recursion  - divide, sort and then merge
    if left<right:
        mid=left+(right-left)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)
    return arr
    
def merge(arr:list,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[]
    R=[]
    for i in range(n1):
        L.append(arr[l+i]) #temp left array
    
    for i in range(n2):
        R.append(arr[m+1+i]) #temp right array

    i,j=0,0
    k=l #for tracking the insertion position in array
    while i<n1 and j<n2:
        #replace actual elements in k depending on whether left/right array has smaller element (left and right is expected to sorted due to previous iterations)
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    #copy remaining elements
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1


def quicksort(arr:list,low,high):
    #pick a pivot, partition the array such that left<pivot<right, recurse on left and right
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
    return arr

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1 #initially -1
    for j in range(low,high):
        #swap with ith element in case elements have value less than pivot
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[i+1],arr[high]=arr[high],arr[i+1] #swap pivot with i+1 th element indicating the last change- expectation is all values are less tha pivot before this and greater after this
    return i+1 #return pivot which is getting fixed at proper position after each iteration
print(quicksort([64,25,12,22,11],0,4))