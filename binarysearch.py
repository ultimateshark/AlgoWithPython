arr1=input("Enter Array values seperated by spaces").split(" ")
arr=[int(x) for x in arr1]
n=int(input("Enter number to be searched"))
arr.sort()
print("Sorted Array",arr)
low,high=0,len(arr)
mid=(low+high)//2
while low<=high:
	if arr[mid]==n:
		print("Found At ",mid+1)
		break
	elif arr[mid]>n:
		high=mid-1
	elif arr[mid]<n:
		low=mid+1
	mid=(low+high)//2
