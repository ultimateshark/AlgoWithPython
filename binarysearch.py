def binarysearch(arr,n):
	low,high=0,len(arr)
	mid=(low+high)//2
	while low<=high:
		if arr[mid]==n:
			return mid
			break
		elif arr[mid]>n:
			high=mid-1
		elif arr[mid]<n:
			low=mid+1
		mid=(low+high)//2

if __name__ == '__main__':
	arr1=input("Enter Array values seperated by spaces").split(" ")
	arr=[int(x) for x in arr1]
	arr.sort()
	print("Sorted Array",arr)
	n=int(input("Enter number to be searched"))
	i=binarysearch(arr,n)
	print("FOUND AT :",i+1)