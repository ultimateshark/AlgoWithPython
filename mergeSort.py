def MergeSort(arr):
	if len(arr)>1:
		mid=len(arr)//2
		L=arr[:mid]
		R=arr[mid:]
		MergeSort(L)
		MergeSort(R)
		Merge(arr,L,R)

def Merge(arr,L,R):
	k,a1,a2=0,0,0
	b1,b2=len(L),len(R)
	while a1<b1 and a2<b2:
		if L[a1]<R[a2]:
			arr[k]=L[a1]
			a1=a1+1
		else:
			arr[k]=R[a2]
			a2=a2+1
		k=k+1

	while a1<b1:
		arr[k]=L[a1]
		a1=a1+1
		k=k+1
	while a2<b2:
		arr[k]=R[a2]
		a2=a2+1
		k=k+1

if __name__ == '__main__':
	arr=list(map(int,input("Enter Elements seperated by space").split(" ")))
	MergeSort(arr)
	print(arr)
	