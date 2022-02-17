import copy
import build_puzzle as bp
from operator import itemgetter


# initialize the array
array = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
print(array)
print('blank array')

# target array
target_array = [[1, 2, 3],
                [8, 0, 4],
                [7, 6, 5]]
print(array)

# list to check for unique values appended
assigned = []

# build puzzle randomly
bp.assign_values(array, assigned)
bp.blank_spot(array)

# built array
print(array)
print('built array')


# check if the randomized puzzle is solvable
if(bp.isSolvable(array)):
    print(array)
    print("Solvable")

# if not solvable, keep trying until a solvable puzzle is made
else:
    while not (bp.isSolvable(array)) and not bp.is_puzzle_blank(array):
        print(array, "Not Solvable")
        array = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
        assigned.clear()
        bp.assign_values(array, assigned)
        bp.blank_spot(array)
        print(array)

print(array, "solvable")

# two list, one for keeping track of arrays that are visited
# other list to keep track of which ways the blank spot are going
visited_states = []
directions = []


# find the location of the blank spot so that the positions can
# be arranged to make a new state
def find_blank(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                return (i, j)


# finds the neighbors or possible moves from a current configuration of the state
# results is a list with each element being a list of size of 3
# each element contains a direction, the configuration of the array,
# the cost of the array
def possible_moves(array, blank_spot):
    i, j = blank_spot
    results = []
    if i > 0:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i - 1][j]
        copy_array[i - 1][j] = 0
        if copy_array not in visited_states:
            results.append(('up', copy_array, get_cost(copy_array)))
    if j > 0:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i][j - 1]
        copy_array[i][j - 1] = 0
        if copy_array not in visited_states:
            results.append(('left', copy_array, get_cost(copy_array)))
    if i < 2:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i + 1][j]
        copy_array[i + 1][j] = 0
        if copy_array not in visited_states:
            results.append(('down', copy_array, get_cost(copy_array)))
    if j < 2:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i][j + 1]
        copy_array[i][j + 1] = 0
        if copy_array not in visited_states:
            results.append(('right', copy_array, get_cost(copy_array)))
    return results


# traverses the problem via DFS on the right side first
# depth limit not yet implemented. As for now, the tree will
# search deeply until the loop counter is hit to prevent continous loop
# to implement: stop the algorithm from finding new possible moves, and
# instead just back track pop from the stack list.
def dfs(array):
    # adds first randomized array to the list
    copy_array = copy.deepcopy(array)
    stack = []
    loop_count = 0
    pmove = []
    visited_states.append(array)
    # limiting the amount of iterations to less than 5000
    # solution may not be found in reasonable time
    while copy_array != target_array and loop_count < 25:
        # each node adds its possible next moves that haven't been visited
        for moves in range(len(possible_moves(copy_array, find_blank(copy_array)))):
            stack.append(possible_moves(
                copy_array, find_blank(copy_array))[moves][1])
            pmove.append(possible_moves(
                copy_array, find_blank(copy_array))[moves][0])
        # the next node to be checked is the right side of the tree
        copy_array = copy.deepcopy(stack.pop(len(stack) - 1))
        visited_states.append(copy_array)
        move_taken = pmove.pop(len(pmove) - 1)
        directions.append(move_taken)
        loop_count += 1
        print(loop_count)


# traverses the problem via BFS
# no depth limit implemented yet
# to implement: need to find where each depth ends,
# not sure how to implement
def bfs(array):
    loop_count = 0
    copy_array = copy.deepcopy(array)
    queue = []
    queue_count = 0
    pmove = []
    visited_states.append(array)

    # first for loop is outside while loop:
    # this just adds the first the possible states or depth 1 possibilities
    # to the queue
    for moves in range(len(possible_moves(copy_array, find_blank(copy_array)))):
        queue.append(possible_moves(
            copy_array, find_blank(copy_array))[moves][1])
        pmove.append(possible_moves(
            copy_array, find_blank(copy_array))[moves][0])
        queue_count += 1
    # while loop runs until copy array is identical to the target array
    while copy_array != target_array and loop_count < 25:
        # iterative for loop to dequeue the queued states
        for arrays in range(queue_count):
            arrays = 0
            # starts with depth 1 very left node
            # checks and see if it is a solution
            # each iteration checks next state in the queue
            copy_array = copy.deepcopy(queue.pop(0))
            move_taken = pmove.pop(0)
            visited_states.append(copy_array)
            directions.append(move_taken)
            # then adds the children of it to the queue
            for moves in range(len(possible_moves(copy_array, find_blank(copy_array)))):
                queue.append(possible_moves(
                    copy_array, find_blank(copy_array))[moves][1])
                pmove.append(possible_moves(
                    copy_array, find_blank(copy_array))[moves][0])
                queue_count += 1
            arrays += queue_count
            loop_count += 1
            print(loop_count)


# cost function heursistic that looks at how many elements are wrong
# in the array compared to the target array
# for each element that is wrong, the cost is increased by 1
def get_cost(array):
    cost = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != target_array[i][j]:
                cost += 1
    return cost


# takes initial array and copy
# priorty queue is the first 3 on depth 1
# sort the queue to turn it into priority based off of cost
# cost is index 3 in inner list
# copy array is now copied from the top of priorty queue
# append the copy array to visted and check if its target
def ucs(array):
    copy_array = copy.deepcopy(array)
    pqueue = []
    loop_count = 0
    for moves in range(len(possible_moves(copy_array, find_blank(copy_array)))):
        pqueue.append(possible_moves(
            copy_array, find_blank(copy_array))[moves])
    sorted(pqueue, key=itemgetter(2))
    copy_array = copy.deepcopy(pqueue.pop(0))
    visited_states.append(copy_array)
    while copy_array[1] != target_array and loop_count < 5:
        for moves in range(len(possible_moves(copy_array[1], find_blank(copy_array[1])))):
            pqueue.append(possible_moves(
                copy_array[1], find_blank(copy_array[1]))[moves])
        sorted(pqueue, key=itemgetter(2))
        copy_array = copy.deepcopy(pqueue.pop(0))
        visited_states.append(copy_array)
        loop_count += 1
        print('pqueue', pqueue)
        print('sorted pqueue', pqueue)
        print()
        print(loop_count)


print("starting blank:", find_blank(array))
print()
# print(possible_moves(array, find_blank(array)))
# print('cost', get_cost(array))
# dfs(array)
# bfs(array)
ucs(array)
print()
print('these are visited states', visited_states)
# print('these are the directions of the zero', directions)
sorted(visited_states, key=itemgetter(2))
print()
# print('these are sorted visitied states', visited_states[0][2])
# A = [[10, 8], [90, 2], [45, 6]]
# print("Sorted List A based on index 0: % s" % (sorted(A, key=itemgetter(0))))
# print("Sorted List A based on index 1: % s" % (sorted(A, key=itemgetter(1))))
