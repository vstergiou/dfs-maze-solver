import graph as G
import pprint
from utils import load_maze



tiny = '''
######
#    #
# # ##
######
'''.strip()



#read and load maze
maze_path = "data/input_maze.txt"
maze_lists = load_maze(maze_path)

#create graph from maze data
demo = G.Graph(maze_lists) 
demo.print_graph()

print(f'Nodes of graph: {demo.vertex_set()}')
print(f'number of graph Nodes: {demo.num_vertices()}')
print(f'contains vertex (1,1):{demo.contains_vertex((1,1))}')
print(f'contains vertex (0,0):{demo.contains_vertex((0,0))}')
demo.add_vertex((0,0))
print(f'Adding vertex (0,0):')
print(f'number of graph Nodes: {demo.num_vertices()}')
print(f'contains vertex (0,00):{demo.contains_vertex((0,0))}')
print(f'Nodes of graph: {demo.vertex_set()}')



