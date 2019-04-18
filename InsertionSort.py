def insersionsort(arr):
	for i in range(1,len(arr)):
		for x in range(i-1,-1,-1):
			if arr[x+1]<arr[x]:
				temp=arr[x+1]
				arr[x+1]=arr[x]
				arr[x]=temp
	return arr

if __name__ == '__main__':
	arr=input("ENTER UNSORTED ARRAY SEPERATED BY SPACES\n").split(" ")
	arr=[int(x) for x in arr]
	sortedarr=insersionsort(arr)
	print(sortedarr)