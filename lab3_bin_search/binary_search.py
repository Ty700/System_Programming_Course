#!/usr/bin/python3

#Overcomplicated this assignment and lost my mind midway through. Enjoy

#returns an array from 0 - n with n being a user input
#actually nvm. Ignored the user input and just gave it a set size of 10 like it asked
def setupArray(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

#counter - not asked for but I always like to see this
class count:
    counter = 0

#I'm tired... it's way past my bed time. 1:20am currently and I usually sleep at 9:30pm
def binary_search(arr, searchFor):
    left = 0
    right = len(arr) - 1
    mid_index = 0

    #handles searching for a number not in range of list
    if(searchFor > arr[len(arr) - 1]):
        return arr[len(arr) - 1]
    
    #handles searching for negatives
    if(searchFor < arr[0]):
        return arr[0]
    
    #typical binary search 
    while(left <= right):
        mid_index = (right + left) // 2

        count.counter += 1

        if(arr[mid_index] < searchFor):
            left = mid_index + 1

        elif(arr[mid_index] > searchFor):
            right = mid_index - 1

        else:
            return (arr[mid_index])

        
#main boss
def main():
    #lenOfArray = int(input("Enter in the length of the array: "))
    #arr = setupArray(lenOfArray)

    arr = setupArray(10) 

    #Am I repeating code? Yes. Will I do anything about it? No. Why? Am Lazy and this do be worky so no fixy.
    print("Found: {0} in {1} tries"
          .format(binary_search(arr, 3), count.counter))
    count.counter = 0

    print("Found: {0} in {1} tries"
          .format(binary_search(arr, 7), count.counter))
    count.counter = 0

    print("Found: {0} in {1} tries"
          .format(binary_search(arr, 11), count.counter))
    count.counter = 0

    print("Found: {0} in {1} tries"
          .format(binary_search(arr, 20), count.counter))
    count.counter = 0

#calls the main boss
if __name__ == "__main__":
    main()