import graph as G
import argparse
from utils import load_maze, to_str
import convert


def find_target_coords(nested_lists): 
    '''
    Scans maze to find start-point and exit-point.
    '''
    width, height = len(nested_lists[0]), len(nested_lists)
    PATH = ['', ' ']
    START_POINT = 'X'

    for row_idx, row in enumerate(nested_lists):
        for col_idx, c in enumerate(row):
            #is node exit
            if any(
                (row_idx == 0,
                row_idx == height-1, 
                col_idx == 0, 
                col_idx == width -1
                )
            ) and nested_lists[row_idx][col_idx] in PATH:
                exit = (row_idx, col_idx)
            #is node start 
            elif nested_lists[row_idx][col_idx] == START_POINT:
                start = (row_idx, col_idx)
                
    return start, exit



        




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True,  help='Path to maze file')
    parser.add_argument("--show", "-s", type=str, required=False,  help='Draw the path')
    args = parser.parse_args()

    #read and load maze
    maze_path = args.file
    maze_lists = load_maze(maze_path)
    
    #create graph from maze data
    demo = G.Graph(maze_lists) 
    print(f'_____Graph_____')  
    demo.print_graph() 
   
    #find start and exit coords
    start_coords, exit_coords = find_target_coords(maze_lists)
    print(f'\nStart coords: {start_coords}')
    print(f'Exit coords: {exit_coords}')
    
    #DFS path from start_coords to exit_coords
    dfs_path = demo.find_path_dfs(start_coords, exit_coords)
    print(f'DFS path: {dfs_path}\n')

    if args.show:
        if dfs_path:
            convert.draw_path(maze_lists, dfs_path)
        else:
            print(f'No path found!')

