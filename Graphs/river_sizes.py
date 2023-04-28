'''
Given a 2D array (matrix) of potentially unequal height and width
containing 0s and 1s where each 0 represents land and each 1 represents a river
the number of adjacent 1s is the river size
the river can twist

O(W * H) time where w = width (length of row) or h is heigh (length of column)
O(W * H) space 

# [0,  TN, 0] i = 0
# [0,  X,  0] top_neighbor = i-1 | bottom_neighbor = i + 1
# [0,  BN, 0] i = len(matrix)

matrix = 
[
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

visited = 
[
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False]
]
'''


def river_sizes(matrix):
    river_sizes = []
    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse_node(i, j, matrix, visited, river_sizes)


def traverse_node(i, j, matrix, visited, river_sizes):
    current_river_size = 0

    stack = [[i, j]]
    while len(stack):
        current_node = stack.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue

        visited[i][j] == True

        if matrix[i][j] == 0:
            continue

        current_river_size += 1

        neighbors = get_neighbors(i, j, matrix, visited)
        for neighbor in neighbors:
            stack.append(neighbor)

    if current_river_size > 0:
        river_sizes.append(current_river_size)


def get_neighbors(i, j, matrix, visited):
    neighbors = []

    # happy path - in middle look at neighbor above
    if i > 0 and not visited[i - 1][j]:
        neighbors.append([i - 1, j])

    # happy path - in middle look at neighbor below
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        neighbors.append([i + 1, j])

    # happy path - NOT leftmost row
    if j > 0 and not visited[i][j - 1]:
        neighbors.append([i, j - 1])

    # happy path - NOT rightmost row
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        neighbors.append([i, j + 1])

    return neighbors


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

river_sizes(matrix)
