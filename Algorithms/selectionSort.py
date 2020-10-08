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

#Receives the unsorted array
def findSmallest(arr):
    #Grab the first element of the array
    smallest = arr[0]
    #The index of the first element of the array
    smallest_index = 0
    #Loop though the array starting with the second element
    for i in range(1, len(arr)):
        #If this element is smaller than the first element
        if arr[i] < smallest:
            #This element is now the smallest element
            smallest = arr[i]
            #Grab the index of the smallest element
            smallest_index = i
    #Return the index of the smallest element in the array
    return smallest_index

#Receives the array to sort
def selectionSort(arr):
    #Creates the empty array that will contain our numbers in ascending order
    newArr = []
    #Loop through the elements of the received array
    for i in range(len(arr)):
        #function findSmallest returns the index of the smallest number in the array
        smallest = findSmallest(arr)
        #Remove the smallest number from the received array
        # and append it to the sorted array
        newArr.append(arr.pop(smallest))
    #Return the sorted array after looping through all the elements
    return newArr

arr = list(map(int, input().rstrip().split()))

print(selectionSort(arr))
