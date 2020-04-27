from graph import Graph
from randomGraph import RandomGraph
from menu import print_menu
from exceptions import exceptionGraph

class Run():

    def __init__(self, file_name):
        self.__fileName = file_name
        self.__commands = { "1":self.__loadFromFile,
                            "2":self.__get_nr_of_vertices,
                            "3":self.__see_vertices,
                            "4":self.__get_degrees,
                            "5":self.__change_cost,
                            "6":self.__verify_edge,
                            "7":self.__add_vertex,
                            "8":self.__add_edge,
                            "9":self.__remove_vertex,
                            "10":self.__remove_edge,
                            "11":self.__copy_graph,
                            "12":self.__print_graph,
                            "13":self.__graph_copy,
                            "14":self.__parse_out,
                            "15":self.__isolated_vertices,
                            "16":self.write_to_file,
                            "17":self.randomGraphGen
        }

    def __loadFromFile(self):
        try:
            with open(self.__fileName, "r") as file:
                first_line = file.readline()
                first_line = first_line.strip().split()
                vertices, edges = int(first_line[0]), int(first_line[1])
                self.__Graph = Graph(vertices)
                for i in range(edges):
                    line = file.readline()
                    line = line.strip().split()
                    vertex1, vertex2, cost = int(line[0]), int(line[1]), int(line[2])
                    self.__Graph.add_edge(vertex1, vertex2, cost)
            print("Graph loaded")
        except IOError:
            raise exceptionGraph("Error while reading file")

    def write_to_file(self):
        print("Give the filename: ")
        fileName = input()
        self.__Graph.save_to_file(fileName)

    def __get_nr_of_vertices(self):
        print(self.__Graph.get_nr_of_vertices())

    def __see_vertices(self):
        print(self.__Graph.parse_keys())

    def __verify_edge(self):
        print("Give vertex 1 and vertex 2: ")
        vertex1 = int(input())
        vertex2 = int(input())
        result = {True: "It is an edge", False: "It is not an edge"}
        print(result[self.__Graph.is_edge(vertex1, vertex2)])

    def __get_degrees(self):
        print("Give a vertex")
        vertex = int(input())
        print("The in degree is: " + str(self.__Graph.get_in_degree(vertex)))
        print("The out degree is: " + str(self.__Graph.get_out_degree(vertex)))

    def __change_cost(self):
        print("Give the edge's first vertex: ")
        vertex1 = int(input())
        print("Give the edge's second vertex: ")
        vertex2 = int(input())
        print(self.__Graph.get_cost(vertex1, vertex2))
        print("Give the new cost for the edge: ")
        new_cost = int(input())
        self.__Graph.change_edge_cost(vertex1, vertex2, new_cost)

    def __add_vertex(self):
        print("Add new vertex: ")
        vertex = int(input())
        self.__Graph.add_vertex(vertex)

    def __add_edge(self):
        print("Give the edge's first vertex: ")
        vertex1 = int(input())
        print("Give the edge's second vertex: ")
        vertex2 = int(input())
        print("Give the edge's cost: ")
        cost = int(input())
        self.__Graph.add_edge(vertex1, vertex2, cost)

    def __isolated_vertices(self):
        print(self.__Graph.isolated_vertices())

    def __remove_vertex(self):
        print("The vertex you want to remove is: ")
        vertex = int(input())
        self.__Graph.remove_vertex(vertex)

    def __remove_edge(self):
        print("You want to remove an edge.")
        print("The edge's first vertex: ")
        vertex1 = int(input())
        print("The edge's second vertex: ")
        vertex2 = int(input())
        self.__Graph.remove_edge(vertex1, vertex2)

    def __copy_graph(self):
        print("Copying graph :)")
        self.__GraphCopy = self.__Graph.copy_the_graph()
        print("The graph is now copied and saved in __GraphCopy")

    def __graph_copy(self):
        print("The vertices of the copied graph are: ")
        print(self.__GraphCopy.parse_keys())
        print("The edges of the copied graph are: ")
        print(self.__GraphCopy.return_edges())

    def __print_graph(self):
        print("The vertices of the graph are: ")
        print(self.__Graph.parse_keys())
        print("The edges of the graph are: ")
        print(self.__Graph.return_edges())

    def __parse_out(self):
        print("Get the vertex: ")
        vertex = int(input())
        out = self.__Graph.parse_out_neighbours(vertex)
        print(out)
        inNeighbours = self.__Graph.parse_in_neighbours(vertex)
        print(inNeighbours)

    def randomGraphGen(self):
        print("Give the number of vertices: ")
        vertices = int(input())
        print("Give the number of edges: ")
        edges = int(input())
        self.__Graph = RandomGraph(vertices,edges)
        print("Give the file name: ")
        fileName = input()
        self.__Graph.save_to_file(fileName)

    def run(self):
        while True:
            print_menu()
            print(">>>")
            command = input()
            if command == "exit":
                return
            elif command in self.__commands:
                try:
                    self.__commands[command]()
                except exceptionGraph as e:
                    print(e)
            else:
                print("Inexistent command")

r = Run("graph1k.txt")
r.run()

