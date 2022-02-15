import random


# assign random values uniquely to the array
def assign_values(array, assigned):
    for i in range(len(array)):
        for j in range(len(array[i])):
            while array[i][j] == 0:
                rand = random.randrange(1, 10)
                if rand not in assigned:
                    array[i][j] = rand
                    assigned.append(rand)
    return array


# find the last spot for the zero
def blank_spot(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 9:
                array[i][j] = 0
    return array


# function to check if the array is blank
# to be used in conjunction with solvable array
# to keep creating new arrays until a sovlable puzzle is found
def is_puzzle_blank(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                count += 1
    return (count >= 8)


"""
The bottom two functions are from geeks for geeks.
They are used to identify if the function is solvable given
the amount of inversions on the original problem.
Since my top two original functions generates the puzzle
at random, there may be instances where the puzzle is not solvable.
Hence the solution I decided to use was that if the problem was not
solvable, was to simply randomize and create a new puzzle that is solvable.
Then the assignment can proceed forward with BFS, DFS, and UCS searches.
"""


# A utility function to count
# inversions in given array 'arr[]'
def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle):

    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])

    # return true if inversion count is even.
    return (inv_count % 2 == 0)
