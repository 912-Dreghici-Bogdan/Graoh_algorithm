from random import randint

from graph import Graph, write_graph_to_file, read_graph_from_file


class UI:
    def __init__(self):
        self.__graphs = []
        self.__current = None

    def add_empty_graph(self):
        if self.__current is None:
            self.__current = 0
        graph = Graph(0, 0)
        self.__graphs.append(graph)
        self.__current = len(self.__graphs) - 1

    def create_random_graph(self):
        vertices = int(input("Nr of vertices: "))
        edges = int(input("Nr of edges: "))
        graph = self.generate_random(vertices, edges)
        if self.__current is None:
            self.__current = 0
        self.__graphs.append(graph)
        self.__current = len(self.__graphs) - 1

    def generate_random(self, vertices, edges):
        if edges > pow (vertices, 2):
            raise ValueError("Too many edges!")
        graph = Graph(vertices, 0)
        i = 0
        while i < edges:
            x = randint(0, vertices - 1)
            y = randint(0, vertices - 1)
            cost = randint(0, 500)
            if graph.add_edge(x, y, cost):
                i += 1
        return graph

    def graph_from_file(self):
        file_name = input("File name: ")
        if self.__current is None:
            self.__current = 0
        graph = read_graph_from_file(file_name)
        self.__graphs.append(graph)
        self.__current = len(self.__graphs) - 1

    def graph_to_file(self):
        current_graph = self.__graphs[self.__current]
        output_file = "output_graph.txt"
        write_graph_to_file(current_graph, output_file)

    def switch_graph(self):
        print("Current graph number: {}".format(self.__current))
        print("Available graphs: 0 - {}".format(str(len(self.__graphs) - 1)))
        number = int(input("Enter the graph number you want to switch to: "))
        if not 0 <= number < len(self.__graphs):
            raise ValueError("Trying to switch to a non existing graph!")
        self.__current = number

    def number_of_vertices(self):
        print("Nr of vertices: {}.".format(self.__graphs[self.__current].number_of_vertices))

    def number_of_edges(self):
        print("Number of edges: {}.".format(self.__graphs[self.__current].number_of_edges))

    def list_all_outbound(self):
        for vertice in self.__graphs[self.__current].parse_vertices():
            output = str(vertice) + " :"
            for outbound in self.__graphs[self.__current].parse_outbound(vertice):
                output = output + " " + str(outbound)
            print(output)

    def list_outbound(self):
        vertex = int(input("Enter the vertex: "))
        output = str(vertex) + " :"
        for y in self.__graphs[self.__current].parse_outbound(vertex):
            output = output + " " + "({}, {})".format(str(vertex), str(y))
        print(output)

    def list_all_inbound(self):
        for vertice in self.__graphs[self.__current].parse_vertices():
            output = str(vertice) + " :"
            for inboud in self.__graphs[self.__current].parse_inbound(vertice):
                output = output + " " + str(inboud)
            print(output)

    def list_inbound(self):
        vertex = int(input("Enter the vertex: "))
        output = str(vertex) + " :"
        for inbound in self.__graphs[self.__current].parse_inbound(vertex):
            output = output + " " + "({}, {})".format(str(inbound), str(vertex))
        print(output)

    def list_all_costs(self):
        for key in self.__graphs[self.__current].parse_cost():
            output = "({}, {})".format(key[0], key[1]) + ": " + str(self.__graphs[self.__current].dictionary_cost[key])
            print(output)

    def parse_all_vertices(self):
        for vertex in self.__graphs[self.__current].parse_vertices():
            print("{}".format(vertex))

    def add_vertex_ui(self):
        vertex = int(input("Enter the new vertex: "))
        added = self.__graphs[self.__current].add_vertex(vertex)

        if added:

            print("Vertex added successfully!")
        else:

            print("Vertex already exists!")

    def delete_vertex(self):
        vertex = int(input("Wanted vertex: "))
        deleted = self.__graphs[self.__current].remove_vertex(vertex)
        if deleted:
            print("Vertex deleted!")
        else:
            print("Vertex doesn't exist!")

    def add_edge(self):
        print("Add an edge (an edge is (x, y))")
        vertex_x = int(input("x: "))
        vertex_y = int(input("y: "))
        cost = int(input("Enter the cost of the edge: "))
        added = self.__graphs[self.__current].add_edge(vertex_x, vertex_y, cost)
        if added:
            print("Edge added!")
        else:
            print("Edge already exists!")

    def remove_edge_ui(self):
        print("Remove an edge (an edge is (x, y))")
        vertex_x = int(input("x: "))
        vertex_y = int(input("y: "))
        deleted = self.__graphs[self.__current].remove_edge(vertex_x, vertex_y)
        if deleted:
            print("Edge deleted!")
        else:
            print("Edge does not exist!")

    def modify_cost_ui(self):
        print("Modify the cost of an edge (an edge is (x, y))")
        vertex_x = int(input("x: "))
        vertex_y = int(input("y: "))
        cost = int(input("Enter the cost of the edge: "))
        mod = self.__graphs[self.__current].change_cost(vertex_x, vertex_y, cost)
        if mod:
            print("Cost modified successfully!")
        else:
            print("Cannot modify the cost, the edge does not exist!")

    def get_in_degree_ui(self):
        vertex = int(input("Enter the vertex:"))
        degree = self.__graphs[self.__current].in_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The in degree of the vertex {} is {}.".format(vertex, degree))

    def get_out_degree_ui(self):
        vertex = int(input("Enter the vertex:"))
        degree = self.__graphs[self.__current].out_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The out degree of the vertex {} is {}.".format(vertex, degree))

    def check_if_edge(self):
        vertex_x = int(input("x: "))
        vertex_y = int(input("y: "))
        edge = self.__graphs[self.__current].find_if_edge(vertex_x, vertex_y)
        if edge is not False:
            print("({}, {}) is an edge and its cost is {}!".format(vertex_x, vertex_y, edge))
        else:
            print("({}, {}) is not an edge!".format(vertex_x, vertex_y))

    def copy_graph(self):
        write_graph_to_file(self.__graphs[self.__current], "copy.txt")

    def print_menu(self):
        print("MENU:\n"
              "0- Exit\n" 
              "1- Create random graph\n"
              "2- Read graph from file\n"
              "3- Write graph in file\n"
              "4- Switch the graph\n" 
              "5- Get the number of vertices\n"
              "6- Get the number of edges\n"
              "7- List the outbound edges of a given vertex\n"
              "8- List all outbound vertices of the graph\n"
              "9- List the inbound edges of a given vertex\n"
              "10- List all inbound vertices of the graph\n"
              "11- List the edges and their costs\n"
              "12- Add a vertex\n"
              "13- Remove a vertex\n"
              "14- Add an edge\n"
              "15- Remove an edge\n"
              "16- Modify the cost of an edge\n"
              "17- Get the in degree of a vertex\n"
              "18- Get the out degree of a vertex\n"
              "19- Check if there is an edge between two given vertices\n"
              "20- Make a copy of the graph\n"
              "21- Add an empty graph\n"
              "22- Parse all the vertices\n")

    def start(self):
        print("Hello!")
        done = False
        self.add_empty_graph()
        command_dict = {"1": self.create_random_graph, "2": self.graph_from_file,
                        "3": self.graph_to_file, "4": self.switch_graph,
                        "5": self.number_of_vertices, "6": self.number_of_edges,
                        "7": self.list_outbound, "8": self.list_all_outbound, "9": self.list_inbound,
                        "10": self.list_all_inbound, "11": self.list_all_costs, "12": self.add_vertex_ui,
                        "13": self.delete_vertex, "14": self.add_edge, "15": self.remove_edge_ui,
                        "16": self.modify_cost_ui, "17": self.get_in_degree_ui, "18": self.get_out_degree_ui,
                        "19": self.check_if_edge, "20": self.copy_graph, "21": self.add_empty_graph,
                        "22": self.parse_all_vertices}
        while not done:
            try:
                self.print_menu()
                option = input("Choose an option from the menu: \n")
                if option == "0":
                    done = True
                elif option in command_dict:
                    command_dict[option]()
                else:
                    print("Bad input!\n")
            except ValueError as ve:
                print(str(ve))
            except FileNotFoundError as fnfe:
                print(str(fnfe).strip("[Errno 2] "))


UI().start()