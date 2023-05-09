'''
You're given a 2D array (matrix) of potentially unequal W x H containing only 0s and 1s
1s are black and 0s and white, and islands are any 1s horizontal or vertically connected not on border layer

write a fn that returns a modified version in input matrix, where all islands are removed. 
an island is removed by replacing it with a 0 (you can mutate the input matrix)

matrix = 
[
    [ 0 , 1, 0, 0],
    [ 0 , 1, 0, 1],
    [ 0 , 1, 1, 0],
    [ 1 , 1, 0, 0],
]

'''

def remove_islands(matrix):
    row_idx = 0
    column_idx = 0
    visited = [[False for _ in row] for row in matrix]
    
    traverse_graph(row_idx, column_idx, visited, matrix)

    return matrix


def traverse_graph(row_idx, column_idx, visited, matrix):
    
    stack = [[row_idx, column_idx]]
    while len(stack):
        node = stack.pop()
        row_idx = node[0]
        column_idx = node[1]
        
        if (visited[row_idx][column_idx]):
            continue 
        if(matrix[row_idx][column_idx] == 0):
            continue
        # check if its in boarder row, column if so, skip it 
        
        # otherwise, flip it to 0 and move along island 
        matrix[row_idx][column_idx] = 0     
        neighbors = get_neighbors(row_idx, column_idx, visited, matrix)
        for neighbor in neighbors:
            stack.append(neighbor)
    
    
    
def get_neighbors (row_idx, column_idx, visited, matrix):
    pass
    # condition1  (not in TOPMOST & Not in visited )
    
    # condition2  (not in LEFTMOST & Not in visited )
    
    # condition3  (not in BOTTOMMOST & Not in visited )
    
    # condition3  (not in RIGHTMOST & Not in visited )
