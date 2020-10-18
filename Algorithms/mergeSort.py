def merge_sort(values): 
    #Enter if the array has more than one element
    if len(values)>1:
        #Divide in two the length of the array
        m = len(values)//2
        #left will store the array from beginning until the
        #element before the middle element
        left = values[:m]
        #right will store the array from the middle element until
        #the end
        right = values[m:]
        #Recursion with the first half
        left = merge_sort(left)
        #Recursion with the second half
        right = merge_sort(right)

        #Empty list for the sorted numbers
        values =[]

        #While the left array and right array has more than
        #zero elements
        while len(left)>0 and len(right)>0:
            #if the first element of the left array
            #is lower than the first element of the
            #right array
            if left[0]<right[0]:
                #append the first element of left to
                #the values array
                values.append(left[0])
                #Pop from left its first element
                left.pop(0)
            #if the first element of right is
            #lower than the first element of left
            else:
                #append the first element of right to
                #the values array
                values.append(right[0])
                #Pop from right its first element
                right.pop(0)

        #Looping through the elements of left
        for i in left:
            #Append its elements to values
            values.append(i)
        #Looping through the elements of right
        for i in right:
            #Append its elements to values
            values.append(i)

    return values

# Input list
a = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(*a)

a = merge_sort(a)

# Print output
print("Sorted array is : ")
print(*a)
