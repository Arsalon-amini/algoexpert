import breadth_first_search

graph = breadth_first_search.Node('A')
graph.add_child('B').add_child('C').add_child('D')
graph.children[0].add_child('E').add_child('F')
graph.children[0].children[1].add_child('I').add_child('J')
graph.children[2].add_child('G').add_child('H')
graph.children[2].children[1].add_child('K')

array = []
bfs_result = graph.breadth_first_search(array)
print(bfs_result)
