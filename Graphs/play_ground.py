matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]


#### PLAYGROUND #####
def riverSizes(matrix):
    river_sizes = []
    visited = [[False for value in matrix_row] for matrix_row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if visited[row][column]:
                continue
            traverse_matrix(visited, river_sizes, row, column, matrix)
    return river_sizes


def traverse_matrix(visited, river_sizes, row, column, matrix):
    nodes_to_explore = [[row, column]]
    current_river = 0

    while len(nodes_to_explore) > 0:
        current_node = nodes_to_explore.pop()

        row_idx = current_node[0]
        column_idx = current_node[1]

        if visited[row_idx][column_idx] == True:
            continue
        visited[row_idx][column_idx] = True

        if matrix[row_idx][column_idx] == 0:
            continue

        current_river += 1

        unvisited_neighbors = get_unvisited_neighbors(
            visited, matrix, row_idx, column_idx)

        for neighbor in unvisited_neighbors:
            nodes_to_explore.append(neighbor)

    if current_river > 0:
        river_sizes.append(current_river)


def get_unvisited_neighbors(visited, matrix, row, column):
    unvisited_neighbors = []

    # condition (not in top row)
    if row > 0 and not visited[row - 1, column]:
        unvisited_neighbors.append([row - 1, column])

    # condition (not in bottom row)
    if row < len(matrix) and not visited[row + 1][column]:
        unvisited_neighbors.append([row + 1, column])

    # condition(not in first column)
    if column > 0 and not visited[row][column-1]:
        unvisited_neighbors.append([row, column - 1])

    # condition (not in last column)
    if column < len(matrix[0]) - 1 and not visited[row][column + 1]:
        unvisited_neighbors.append([row, column + 1])

    return unvisited_neighbors


riverSizes(matrix)
