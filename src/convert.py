'''
Helper functions to convert Graph from other formats.
'''

from utils import to_nested_list, to_str
from collections import OrderedDict
from vertex import Vertex

__all__ = [
    "maze_to_graph", 
    "draw_path"
]

PATH = ['', ' ', 'X']
WALL = ['#']


def get_neighbors(coords, nested_list):
    '''
    Returns a list of the neighbors of a cell. 
    '''
    row, col = coords

    visited = (
        check_node((row - 1, col), nested_list),  # Down
        check_node((row + 1, col), nested_list),  # Up
        check_node((row, col - 1), nested_list),  # Right
        check_node((row, col + 1), nested_list),  # Left
    )
    return [v for v in visited if isinstance(v, tuple)]


def check_node(coords, nested_list):
    '''
    Checks if a node is PATH or WALL.
    '''
    width, height = len(nested_list[0]), len(nested_list)
    row, col = coords

    if any((row < 0, row > height - 1, col < 0, col > width - 1)):
        #(row,col) is out of borders
        return False
    elif nested_list[row][col] in PATH:
        #is PATH
        return (row, col)
    else:
        #is WALL
        return False


def to_adjlist(nested_list):
    '''
    Converts a list of lists to adjacency list.
    '''
    adjlist = OrderedDict()

    for row_idx, row in enumerate(nested_list):
        for col_idx, c in enumerate(row):
            coords = (row_idx, col_idx)
            if check_node(coords, nested_list):
                current_vertex = Vertex(coords, get_neighbors(coords, nested_list))
                adjlist.update({coords: current_vertex})

    return adjlist


def maze_to_graph(data):

    if isinstance(data, list):
        return to_adjlist(data)

    elif isinstance(data, str): 
        return to_adjlist(to_nested_list(data))


def draw_path(nested_lists, dfs_path):

    for row_idx, row in enumerate(nested_lists):
        for col_idx, c in enumerate(row):
            if (row_idx, col_idx) in dfs_path:
                nested_lists[row_idx][col_idx] = 'x'
    
    #print ASCII maze with path
    print('--------- Maze solved ---------')
    for line in nested_lists:
        print(to_str(line))