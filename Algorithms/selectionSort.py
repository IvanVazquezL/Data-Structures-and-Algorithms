#Selection Sort
#
# The selection sort algorithm sorts an array by repeatedly
# finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning. The
# algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element
# (considering ascending order) from the unsorted subarray is 
# picked and moved to the sorted subarray.
#
# Time Complexity: O(n^2)
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr = list(map(int, input().rstrip().split()))

print(selectionSort(arr))
