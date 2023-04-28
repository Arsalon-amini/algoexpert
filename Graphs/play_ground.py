# import breadth_first_search

# graph = breadth_first_search.Node('A')
# graph.add_child('B').add_child('C').add_child('D')
# graph.children[0].add_child('E').add_child('F')
# graph.children[0].children[1].add_child('I').add_child('J')
# graph.children[2].add_child('G').add_child('H')
# graph.children[2].children[1].add_child('K')

# array = []
# bfs_result = graph.breadth_first_search(array)
# print(bfs_result)

edges = [
    [1, 2],
    [3],
    [],
    [4, 2],
    []
]

WHITE, GREY, BLACK = 0, 1, 2


def cycle_in_graph(edges):
    colors = [WHITE for _ in range(len(edges))]
    num_nodes = len(edges)

    for node in range(num_nodes):
        if colors[node] == BLACK:
            continue

        has_cycle = dfs_and_color(edges, node, colors)
        if has_cycle:
            return True
        return False


def dfs_and_color(edges, node, colors):
    colors[node] = GREY
    node_neighbors = edges[node]
    for neighbor in node_neighbors:
        neighbor_color = colors[neighbor]

        if neighbor_color == BLACK:
            continue
        if neighbor_color == GREY:
            return True

        has_cycle = dfs_and_color(edges, neighbor, colors)
        if has_cycle:
            return True

    return False


cycle_in_graph(edges)
