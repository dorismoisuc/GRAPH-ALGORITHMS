from graph import Graph
from random import choice
from exceptions import exceptionGraph

# a class for generating random graph
class RandomGraph():
    def __init__(self, vertices, edges):
        self.__randomG = Graph(vertices)
        self.__generate(vertices, edges)

    def __generate(self, vertices, edges):
        vertices = [i for i in range(vertices)]
        costs = [0]
        for i in range(1, 101):
            costs.append(i)
            costs.append(-i)
        index = 0
        while index < edges:
            vertex1 = choice(vertices)
            vertex2 = choice(vertices)
            cost = choice(costs)
            try:
                self.__randomG.add_edge(vertex1, vertex2, cost)
                index += 1
            except exceptionGraph:
                pass

    # saves the graph to a file
    def save_to_file(self, fileName):
        with open(fileName,"w") as f:
            f.write(str(self))


    def __str__(self):
        string = ""
        string+= "The vertices of the random graph are: "
        string+= str(self.__randomG.parse_keys())
        string+='\n'
        string+="The edges of the random graph are: "
        string+= str(self.__randomG.return_edges())
        string+='\n'
        string+="The costs of the random graph are: "
        string+=str(self.__randomG.return_costs())
        string+='\n'
        return string

