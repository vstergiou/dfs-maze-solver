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

print(f'contains edge (1,1) - (2,1) :{demo.contains_edge((1,1),(2,1))}')

print(f'Neighbors of (1,1): {demo.neighbors((1,1))}')
print(f'Degree of (1,1): {demo.degree((1,1))}')
print(f'contains edge (1,1) - (1,5) :{demo.contains_edge((1,1),(1,5))}')
demo.add_edge((1,1),(1,5))
print(f'Adding edge (1,1) - (1,5) :')

print(f'contains edge (1,1) - (1,5) :{demo.contains_edge((1,1),(1,5))}')
print(f'Neighbors of (1,1): {demo.neighbors((1,1))}')
print(f'Degree of (1,1): {demo.degree((1,1))}')