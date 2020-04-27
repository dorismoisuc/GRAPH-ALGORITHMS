from exceptions import exceptionGraph
import copy


class Graph(object):
    def __init__(self, vertices):
        self.__dictionaryIn = {}
        self.__dictionaryOut = {}
        self.__dictionaryCosts = {}

        for i in range(vertices):
            self.__dictionaryOut[i] = []
            self.__dictionaryIn[i] = []

    # returns a copy of all vertex keys

    def parse_keys(self):
        # The list() constructor returns a list.
        # If no parameters are passed, it returns an empty list
        # If iterable is passed as a parameter, it creates a list consisting of iterable's items.
        return list(self.__dictionaryOut.keys())

    # returns a copy of all out neighbours of 'vertex'
    def parse_out_neighbours(self, vertex):
        try:
            return list(self.__dictionaryOut[vertex])
        except KeyError:
            raise exceptionGraph("Inexistent vertex")

    # returns a copy of all out neighbours of 'vertex'
    def parse_in_neighbours(self, vertex):
        try:
            return list(self.__dictionaryIn[vertex])
        except KeyError:
            raise exceptionGraph("Inexistent vertex")

    # checks if there is an edge from vertex1 to vertex2
    # returns true if there is an edge from vertex1 to vertex2, false otherwise
    def is_edge(self, vertex1, vertex2):
        try:
            return vertex2 in self.__dictionaryOut[vertex1]
        except KeyError:
            raise exceptionGraph("No edge between these 2 vertices in the graph")

    """
    Function to add an edge from vertex1 to vertex 2 with a cost to the graph
    May have exceptions if: the edge already exists and the vertices aren't valid.
    """
    def add_edge(self, vertex1, vertex2, cost):
        exception_message = ""
        if self.is_edge(vertex1, vertex2):
            exception_message += "The edge from vertex1 to vertex 2 already exists"
        if len(exception_message) > 0:
            raise exceptionGraph(exception_message)
        self.__dictionaryOut[vertex1].append(vertex2)
        self.__dictionaryIn[vertex2].append(vertex1)
        self.__dictionaryCosts[(vertex1, vertex2)] = cost

    """
    Function to add the vertex to the graph, as an isolated vertex
    Returns an exception if the vertex already exists in the graph
    """
    def add_vertex(self, vertex):
        if vertex in self.parse_keys():
            raise exceptionGraph("This vertex already exists in the graph")
        self.__dictionaryOut[vertex] = []
        self.__dictionaryIn[vertex] = []

    # returns the cost of the edge from vertex1 to vertex2
    def get_cost(self, vertex1, vertex2):
        if self.is_edge(vertex1, vertex2):
            return self.__dictionaryCosts[(vertex1, vertex2)]

    # returns the isolated vertices
    def isolated_vertices(self):
        vertices = []
        for key in self.parse_keys():
            if self.__dictionaryIn[key] == [] and self.__dictionaryOut == []:
                vertices.append(key)
        return vertices[:]

    # removes the vertex from the graph
    # returns an exception if the vertex doesn't exist in the graph
    def remove_vertex(self, vertex):
        if vertex not in self.parse_keys():
            raise exceptionGraph("Vertex doesn't exist")
        for vertex2 in self.__dictionaryOut[vertex]:
            self.__dictionaryIn[vertex2].remove(vertex)
            del self.__dictionaryCosts[(vertex, vertex2)]
        for vertex2 in self.__dictionaryIn[vertex]:
            self.__dictionaryOut[vertex2].remove(vertex)
            del self.__dictionaryCosts[(vertex2, vertex)]
        del self.__dictionaryOut[vertex]
        del self.__dictionaryIn[vertex]

    # removes the edge (vertex1, vertex2) from the graph
    # returns an exception if edge (vertex1, vertex2) is not existent
    def remove_edge(self, vertex1, vertex2):
        if not self.is_edge(vertex1, vertex2):
            raise exceptionGraph("This edge doesn't exist")
        del self.__dictionaryCosts[(vertex1, vertex2)]
        self.__dictionaryOut[vertex1].remove(vertex2)
        self.__dictionaryIn[vertex2].remove(vertex1)

    # returns an integer containing the number of vertices in the graph
    def get_nr_of_vertices(self):
        return len(self.parse_keys())

    # returns an integer having the OUT degree of the vertex
    # if vertex is a valid vertex in the graph, else it returns an exception
    def get_out_degree(self, vertex):
        try:
            return len(self.__dictionaryOut[vertex])
        except KeyError:
            raise exceptionGraph("The vertex doesn't exist")

    # returns an integer having the IN degree of the vertex
    # if vertex is a valid vertex in the graph, else it returns an exception
    def get_in_degree(self, vertex):
        try:
            return len(self.__dictionaryIn[vertex])
        except KeyError:
            raise exceptionGraph("The vertex doesn't exist")

    # changes the cost of an edge (vertex1, vertex2)
    # if the edge exists in the graph, else it returns an exception
    def change_edge_cost(self, vertex1, vertex2, cost):
        if (vertex1, vertex2) in self.__dictionaryCosts:
            self.__dictionaryCosts[(vertex1, vertex2)] = cost
        else:
            raise exceptionGraph("The edge doesn't exist")

    # creates a copy of the graph and
    # returns the copy of the graph
    def copy_the_graph(self):
        new_graph = Graph(10)
        new_graph.__dictionaryIn = copy.deepcopy(self.__dictionaryIn)
        new_graph.__dictionaryOut = copy.deepcopy(self.__dictionaryOut)
        new_graph.__dictionaryCosts = copy.deepcopy(self.__dictionaryCosts)
        return new_graph

    # returns an iterable containing all the edges
    def return_edges(self):
        edges = []
        for edge in self.__dictionaryCosts:
            edges.append(edge)
        return edges[:]

    # returns an iterable containing all the costs
    def return_costs(self):
        costs = []
        for cost in self.__dictionaryCosts:
            costs.append(self.__dictionaryCosts[cost])
        return costs[:]

    # saves the graph to a file
    def save_to_file(self, fileName):
        with open(fileName,"w") as f:
            f.write(str(self))

    def __str__(self):
        string = ""
        for key in self.__dictionaryCosts:
            string += "Vertex1: "
            string+= str(key[0])
            string+= " Vertex2: "
            string+=str(key[1])
            string+= " The cost: "
            string+=str(self.__dictionaryCosts[key])
            string+='\n'
        return string
