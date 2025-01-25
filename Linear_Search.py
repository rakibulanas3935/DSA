def linear_search(arr,value):
    size=len(arr)
    for index in range(0,size):
        if(arr[index]==value):
            return index
    return -1


arr=[3,4,5,6,4,3,7]
res=linear_search(arr,10)
print(res)