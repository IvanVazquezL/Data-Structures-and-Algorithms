##Version book corrected without prints

#It receives the array and the value to search
def binary_search(list, item):
    #The lowest index of the array
    low = 0
    #The highest index of the array
    high = len(list)-1

    #Loop while low is less than high or when both values are equal
    #Check until there is only one element left in the array
    while low <= high:
        #Find the middle index
        mid = (round((high-low)/2))+low
        #Get the number of the middle index
        guess = list[mid]

        if guess == item:
            #If the guessed number is equal to searched value
            #Return the index of that number
            return mid
        if guess > item:
            #if the guessed number is higher than the searched value
            #Change the highest index of the array to the
            # middle index minus one
            # This way you keep the lower half
            high = mid -1
        else:
            #If the guessed number is not higher than the searched value
            #Change the lowest index of the array to there
            # middle index plus one
            # This way you keep the upper half
            low = mid + 1

    #If the searched value is not found, return None
    return None

my_list = list(range(1,11))

print(binary_search(my_list,6))
