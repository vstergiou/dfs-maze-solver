import csv

def load_maze(path):
    '''
    Reads maze input file from path and returns list of lists.
    '''
    with open(path, newline='') as f:
        reader = csv.reader(f)
        maze_lists = list(reader)

    return maze_lists


def to_nested_list(s, delim='\n'):
    return [list(e) for e in s.split(delim)]


def to_str(l, delim=''):
    p = ""
    for row in l:
        p += "".join([str(e) for e in row]) + delim
    return p


