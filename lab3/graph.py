from exceptions import exceptionGraph
import copy


class Graph(object):
    def __init__(self, vertices):
        self._vertices = vertices
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

    def get_costs(self):
        return self.__dictionaryCosts

    def get_edges(self):
        return len(self.__dictionaryCosts)

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


    def set_cost(self,x,y,cost):
        self.__dictionaryCosts[x,y]=cost

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

#
#
#                !!! LAB 3 FUNCTIONS !!!
#
#

    """
    returns the matrix for the graph
    when the line is = column, the position will have the value 0
    if there is an edge from vertex1 to vertex2, on line[vertex1] and column[vertex2]
    will be the cost of this edge 
    otherwise, there will be infinity
    """
    def get_matrix(self):
        matrix = [[0 for it in range(self._vertices)]for it2 in range(self._vertices)]
        for vertex in range(self._vertices):
            for anotherVertex in range(self._vertices):
                if vertex==anotherVertex:
                    matrix[vertex][anotherVertex]=0
                elif self.is_edge(vertex,anotherVertex):
                    matrix[vertex][anotherVertex]=self.get_cost(vertex,anotherVertex)
                else:
                    matrix[vertex][anotherVertex]=float('inf')
        return matrix

    # verifies if there are any negative costs cycles in
    # the graph
    # if there are
    # it raises an exception

    def validator_negative_costs(self,matrix):
        for vertex1 in range(self._vertices):
            for vertex2 in range(self._vertices):
                if matrix[vertex1][vertex2]+matrix[vertex2][vertex1]<0:
                    raise exceptionGraph("It has negative cost cycles!")


        '''
        initializes a matrix called NEXT which will have:
           * if there is an edge from vertex1 to vertex2
             -> on the position from line[vertex1] and column[vertex2] will be the value vertex2
           * if line=column there will be the value [line]
        it will contain in the end a vertex index (column-vertex's indice)
        if a lower cost walk was
        found from the line-vertex to column-vertex
        '''
    def matrix_next(self):

        self.next = [[None for vertex1 in range(self._vertices)]for vertex2 in range(self._vertices)]
        for vertex in range(self._vertices):
            for vertex2 in range(self._vertices):
                if self.is_edge(vertex,vertex2):
                    self.next[vertex][vertex2]=copy.deepcopy(vertex2)
                elif vertex==vertex2:
                    self.next[vertex][vertex2] = copy.deepcopy(vertex2)

    # recreates the path from v1 to v2, parsing the matrix's next
    # starting from v1 until v2

    def path(self, v1, v2):
        print("HERE")
        if self.next[v1][v2]==None:
            return []

        path = [v1]
        while v1!=v2:
            v1 = self.next[v1][v2]
            path.append(copy.deepcopy(v1))
        return path

    # computes a matrix multiplication
    # and adds it to the series
    # extend
    def matrix_multiplication(self, givenMatrix1, givenMatrix2):
        matrix = givenMatrix1
        for vertex1 in range(self._vertices):
            for vertex2 in range(self._vertices):
                for vertex3 in range(self._vertices):
                    if (matrix[vertex1][vertex3]+givenMatrix2[vertex3][vertex2]<matrix[vertex1][vertex2]):
                        matrix[vertex1][vertex2]=min((matrix[vertex1][vertex3]+givenMatrix2[vertex3][vertex2]),matrix[vertex1][vertex2])
                        self.next[vertex1][vertex2]=copy.deepcopy(self.next[vertex1][vertex3])
        return matrix


    '''
    computes the lowest cost between 2 vertices
    returns the cost and the path
    intermediate -> list of all intermediate matrices
    initial_matrix -> the initial matrix of the graph
    next -> a matrix that contains the vertex that follows after a lowest
            cost was found
    '''
    def lowest_cost_walk(self,vertex1,vertex2):
        intermediate = []
        initial_matrix = self.get_matrix()
        self.matrix_next()
        intermediate.append(copy.deepcopy(initial_matrix))
        for it in range(1,(self._vertices)-1):
            intermediates = copy.deepcopy((intermediate[it-1]))
            intermediate.append(copy.deepcopy(self.matrix_multiplication(intermediates,initial_matrix)))

        self.validator_negative_costs(intermediate[-1])
        path_cost = intermediate[-1][vertex1][vertex2]
        path = self.path(vertex1,vertex2)
        write_graph(self)
        print()
        for matrices in intermediate:
            for vertex in range(self._vertices):
                print(*matrices[vertex], sep=' ')
            print()
        print()
        return path_cost,path

def read_graph_from_file(file_name):
    with open(file_name,"r") as f:
        lines = f.readlines()
        first_line = True
        for line in lines:
            if first_line ==True:
                parameters = line.split()
                vertices = int(parameters[0])
                edges = int(parameters[1])
                graph = Graph(vertices)
            if first_line == False :
                line.strip()
                parameters = line.split(' ')
                graph.add_edge(int(parameters[0]), int(parameters[1]),int(parameters[2]))
            first_line = False
        return graph


def write_graph(Graph):
    print("Number of vertices: "+str(Graph.get_nr_of_vertices()))
    print ("Number of edges: "+ str(Graph.get_edges()))
    for vertex in Graph.get_costs().keys():
        print(str(vertex[0])+'->'+str(vertex[1])+' cost: '+str(Graph.get_costs()[vertex]))
