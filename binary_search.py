def binary_search(arr,value):
    size=len(arr)
    start=0
    end=size-1

    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==value):
            return mid
        elif (arr[mid]>value):
            end=mid-1
        elif (arr[mid]<value):
            start=mid+1

    return -1

arr=1,2,7,8,9,12,32,34

res=binary_search(arr,90)
print(res)
