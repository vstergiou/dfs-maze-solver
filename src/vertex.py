class Vertex:
    """
    A representation of a cell in the maze as a Vertex of the graph.
    :param coords: Coordinates (row, col)
    :type  coords: tuple
    :param neighbors: List of the coords of the neighboring vertices)
    :type  neighbors: list
    :param parent: Reference to Vertex, used to create the path from start to exit.
    :param type: Vertex or None
    """
    def __init__(self, coords, neighbors=None):
        self.coords = coords
        if neighbors:
            self.neighbors = neighbors
        else:
            self.neighbors = []

        self.parent = None 
    
    def __len__(self):
        return len(self.neighbors)
    
    def __repr__(self):
        return f"Neighbors: {self.neighbors}"

    