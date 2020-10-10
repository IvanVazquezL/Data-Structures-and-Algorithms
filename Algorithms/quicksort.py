def quicksort(array):
    #If the array is empty or only has one element return the array
    if len(array)<=1:
        return array
    else:
        #the first element of the array will be our pivot
        pivot = array[0]
        #Starting from the seconde element of the array
        #Create an array with the numbers that are lower or equal to the pivot
        less = [i for i in array[1:] if i<= pivot]
        #Create an array with the numbers that are greater than the pivot
        greater = [i for i in array[1:] if i> pivot]

        #Send the sub arrays into recursion and add the pivot between them
        return quicksort(less) + [pivot] + quicksort(greater)



print(quicksort([]))
print(quicksort([20]))
print(quicksort([10,5,2,3]))
