def FindPeak(arr):
    mid=len(arr)//2
    if arr[mid+1]>arr[mid]:
        FindPeak(arr[mid:])
    elif arr[mid-1]>arr[mid]:
        FindPeak(arr[:mid])
    else:
        return arr[mid]

if __name__=="__main__":
    arr=str(input("Enter values of array seperated by ,")).split(",")
    print(FindPeak(arr))
