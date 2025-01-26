def bubble_sort(arr):
    n=len(arr)
    for j in range(0,n-1):
        for i in range(0,n-j-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    
    return arr

arr=[64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))