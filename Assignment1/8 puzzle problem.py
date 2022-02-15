import copy
import build_puzzle as bp


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


def find_blank(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                return (i, j)


def possible_moves(array, blank_spot):
    i, j = blank_spot
    results = []
    if i > 0:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i - 1][j]
        copy_array[i - 1][j] = 0
        if copy_array not in visited_states:
            results.append(('up', copy_array, (i - 1, j)))
    if j > 0:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i][j - 1]
        copy_array[i][j - 1] = 0
        if copy_array not in visited_states:
            results.append(('left', copy_array, (i, j - 1)))
    if i < 2:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i + 1][j]
        copy_array[i + 1][j] = 0
        if copy_array not in visited_states:
            results.append(('down', copy_array, (i + 1, j)))
    if j < 2:
        copy_array = copy.deepcopy(array)
        copy_array[i][j] = copy_array[i][j + 1]
        copy_array[i][j + 1] = 0
        if copy_array not in visited_states:
            results.append(('right', copy_array, (i, j + 1)))

    return results


def dfs(array, target):
    copy_array = copy.deepcopy(array)
    stack = []
    loop_count = 0
    pmove = []
    visited_states.append(array)
    # limiting the amount of iterations to less than 5000
    # solution may not be found in reasonable time
    while copy_array != target and loop_count < 5000:
        for moves in range(len(possible_moves(copy_array, find_blank(copy_array)))):
            stack.append(possible_moves(
                copy_array, find_blank(copy_array))[moves][1])
            pmove.append(possible_moves(
                copy_array, find_blank(copy_array))[moves][0])
        if stack[0] == 0:
            print('no more possible moves')
            break
        else:
            copy_array = copy.deepcopy(stack.pop(len(stack) - 1))
            visited_states.append(copy_array)
            move_taken = pmove.pop(len(pmove) - 1)
            directions.append(move_taken)
            loop_count += 1
            print(loop_count)


print("starting blank:", find_blank(array))
print()
# dfs(array, target_array)
print()
print(visited_states)
print(directions)
