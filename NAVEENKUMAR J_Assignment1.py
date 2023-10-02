#Assignment 1
#Done by NAVEENKUMAR J

'''Assignment - 01:

You are given an array of integers, and you are required to sort this array using one of the following sorting algorithms:
Bubble Sort, Selection Sort, or Insertion Sort.
Your task is to implement the chosen sorting algorithm and analyze its time complexity.'''

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
A=[5, 2, 9, 1, 5, 6]
print(*insertion(A))
