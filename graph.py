import copy


class Graph:
    def __init__(self, number_of_vertices, number_of_edges):
        self.__number_of_vertices = number_of_vertices
        self.__number_of_edges = number_of_edges
        self.ins = {}
        self.outs = {}
        self.costs = {}
        for index in range(number_of_vertices):
            self.ins[index] = []
            self.outs[index] = []

    @property
    def dictionary_cost(self):
        return self.costs

    @property
    def dictionary_in(self):
        return self.ins

    @property
    def dictionary_out(self):
        return self.outs

    @property
    def number_of_vertices(self):
        return self.__number_of_vertices

    @property
    def number_of_edges(self):
        return self.__number_of_edges

    def parse_vertices(self):
        vertices = list(self.ins.keys())
        for v in vertices:
            yield v

    def parse_inbound(self, x):
        for y in self.ins[x]:
            yield y

    def parse_outbound(self, x):
        for y in self.outs[x]:
            yield y

    def parse_cost(self):
        keys = list(self.costs.keys())
        for key in keys:
            yield key

    def add_vertex(self, x):
        if x in self.ins.keys() and x in self.outs.keys():
            return False

        self.ins[x] = []
        self.outs[x] = []
        self.__number_of_vertices += 1
        return True

    def remove_vertex(self, x):
        if x not in self.ins.keys() and x not in self.outs.keys():
            return False

        self.ins.pop(x)
        self.outs.pop(x)

        for key in self.ins.keys():
            if x in self.ins[key]:
                self.ins[key].remove(x)
            elif x in self.outs[key]:
                self.outs[key].remove(x)
        keys = list(self.costs.keys())

        for key in keys:
            if key[0] == x or key[1] == x:
                self.costs.pop(key)
                self.__number_of_edges -= 1
        self.__number_of_vertices -= 1
        return True

    def in_degree(self, x):
        if x not in self.ins.keys():
            return -1
        return len(self.ins[x])

    def out_degree(self, x):
        if x not in self.outs.keys():
            return -1
        return len(self.outs[x])

    def add_edge(self, x, y, cost):
        if x in self.ins[y]:
            return False
        elif y in self.outs[x]:
            return False
        elif (x, y) in self.costs.keys():
            return False
        self.ins[y].append(x)
        self.outs[x].append(y)
        self.costs[(x, y)] = cost
        self.__number_of_edges += 1
        return True

    def remove_edge(self, x, y):
        if x not in self.ins.keys() or y not in self.ins.keys() or x not in self.outs.keys() or y not in self.outs.keys():
            return False
        if x not in self.ins[y]:
            return False
        elif y not in self.outs[x]:
            return False
        elif (x, y) not in self.costs.keys():
            return False
        self.ins[y].remove(x)
        self.outs[x].remove(y)
        self.costs.pop((x, y))
        self.__number_of_edges -= 1
        return True

    def find_if_edge(self, x, y):
        if x in self.ins[y]:
            return self.costs[(x, y)]
        elif y in self.outs[x]:
            return self.costs[(x, y)]
        return False

    def change_cost(self, x, y, cost):
        if (x, y) not in self.costs.keys():
            return False
        self.costs[(x, y)] = cost
        return True

def write_graph_to_file(graph, file):
    file = open(file, "w")
    first_line = str(graph.number_of_vertices) + ' ' + str(graph.number_of_edges) + '\n'
    file.write(first_line)

    if len(graph.dictionary_cost) == 0 and len(graph.dictionary_in) == 0:
        raise ValueError("There is nothing that can be written!")

    for edge in graph.dictionary_cost.keys():
        new_line = "{} {} {}\n".format(edge[0], edge[1], graph.dictionary_cost[edge])
        file.write(new_line)

    for vertex in graph.dictionary_in.keys():
        if len(graph.dictionary_in[vertex]) == 0 and len(graph.dictionary_out[vertex]) == 0:
            new_line = "{} \n".format(vertex)
            file.write(new_line)
    file.close()


def read_graph_from_file(filename):
    file = open(filename, "r")
    line = file.readline()
    line = line.strip()
    vertices, edges = line.split(' ')
    graph = Graph(int(vertices), int(edges))
    line = file.readline().strip()
    while len(line) > 0:
        line = line.split(' ')
        if len(line) == 1:
            graph.dictionary_in[int(line[0])] = []
            graph.dictionary_out[int(line[0])] = []
        else:
            graph.dictionary_in[int(line[1])].append(int(line[0]))
            graph.dictionary_out[int(line[0])].append(int(line[1]))
            graph.dictionary_cost[(int(line[0]), int(line[1]))] = int(line[2])
        line = file.readline().strip()
    file.close()
    return graph