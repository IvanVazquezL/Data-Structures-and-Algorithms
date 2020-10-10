def sumRec(arr):
    if not arr:
        return 0
    else:
        return arr.pop() + sumRec(arr)

def countRec(arr):
    if not arr:
        return 0
    else:
        arr.pop()
        return 1  + countRec(arr)

def maxRec(arr,maxNum):
    if not arr:
        return maxNum
    else:
        number = arr.pop()
        if number > maxNum:
            maxNum = number

        return maxRec(arr,maxNum)

def binarySearch(arr, search, high, low):
    if low>high:
        return None
    else:
        middle = (low+high)//2
        if arr[middle] == search:
            return middle
        elif arr[middle] < search:
            return binarySearch(arr,search,high,middle+1)
        else:
             return binarySearch(arr,search,middle-1,low)

arr = [2,5,8,12,16,23,38,56,72,91]
print(sumRec(arr))
arr = [2,5,8,12,16,23,38,56,72,91]
print(countRec(arr))
arr = [2,5,8,12,16,23,38,56,72,91]
print(maxRec(arr,0))
arr = [2,5,8,12,16,23,38,56,72,91]
print(binarySearch(arr,12,len(arr)-1,0))
