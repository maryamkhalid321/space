def binary_search(arr,target,left,right):
    if left>right:
        return-1
    mid=(left+right)//2  
    if arr[mid]==target:
        return mid
    if target<arr[mid]:
        return binary_search(arr,target,left,mid-1)
    else:
        return binary_search(arr,target,mid+1,right)
array= [1,3,5,7,9,11]
target=7
result=binary_search(array,target,0,len(array)-1)    
if result !=-1:
    print("element found at index:", result)
else:
    print('element not found')