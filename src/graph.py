'''
Base class for undirected graphs.
A graph stores vertices and edges with the use of the Adjancency List `self._graph`
Graph holds undirected edges.
Vertices are 'vertex.Vertex' objects.
'''

from copy import deepcopy
import pprint
from collections import deque
from vertex import Vertex
import convert

class Graph:
    def __init__(self,input_graph_data=None):

        if input_graph_data is None:
            self._graph = {}
        elif isinstance(input_graph_data, dict):
            self._graph = deepcopy(input_graph_data)
        elif isinstance(input_graph_data, list):
            self._graph = convert.maze_to_graph(input_graph_data)
    
    def contains_vertex(self,v):
        try: 
            return v in self._graph.keys()
        except TypeError:
            return False
    
    def contains_edge(self, u, v):

        if u not in self._graph.keys():
            raise AttributeError("The source '%s' is not in the graph" % u)
        if v not in self._graph.keys():
            raise AttributeError("The target '%s' is not in the graph" % v)

        try:
            return u in self._graph[v].neighbors and v in self._graph[u].neighbors
        except TypeError:
            return False

    def add_vertex(self,v):

        if v is None:
            raise ValueError("Node cannot be None.")
        
        if v not in self._graph.keys():
            new_vertex = Vertex(v , [])
            self._graph.update({v:new_vertex})
    
    def add_edge(self, u, v):

        if u is None or v is None:
            raise ValueError("Node cannot be None.")

        #add vertices u,v if not already in the graph 
        if v not in self._graph.keys():
            new_vertex = Vertex(v , [])
            self._graph.update({v:new_vertex})
        
        if u not in self._graph.keys():
            new_vertex = Vertex(u , [])
            self._graph.update({u:new_vertex})

        #make u,v neighbors
        if u not in self._graph[v].neighbors:
            self._graph[v].neighbors.append(u)
        if v not in self._graph[u].neighbors:
            self._graph[u].neighbors.append(v)
        
    def num_vertices(self):
        
        return len(set(self._graph.keys()))
    
    def num_edges(self):
        return sum(len(self._graph[v].neighbors) for v in self._graph.keys()) // 2
        
    def vertex_set(self):

        return set(self._graph.keys())
    
    def neighbors(self, v):
        return set(self._graph[v].neighbors)

    def degree(self,v):
        return len(self._graph[v].neighbors)


    

    def print_graph(self):
        pretty_print = pprint.PrettyPrinter()
        pretty_print.pprint(self._graph)
        

  
    def find_path_dfs(self, s, t):
        """
        Explores the Adjancency List `self._graph` for a path from `s` to `t`.
        If found, returns a list with the path.
        Otherwise, returns False.
        """

        #s,t must be in the graph.
        if s not in self._graph.keys():
            raise AttributeError("The source '%s' is not in the graph" % s)
        if t not in self._graph.keys():
            raise AttributeError("The target '%s' is not in the graph" % t)

        stack = deque()
        visited = set()

        root = self._graph[s]
        stack.append(root)

        while stack:
            current_vertex = stack.pop()
            visited.add(current_vertex)

            if current_vertex.coords == t:
                return self.construct_path(current_vertex)

            # Find adjacent edges that haven't been visited
            for coords in current_vertex.neighbors:
                next_vertex = self._graph[coords]
                if next_vertex not in visited:
                    next_vertex.parent = current_vertex
                    stack.append(next_vertex)

        return False
    

    def construct_path(self, curr):
        '''
        Helper function to construct the list with the path.
        It converts a linked-list to a python list.
        '''
        path = deque()
        while curr !=None:
            path.appendleft(curr.coords)
            curr = curr.parent

        return list(path)
        
        