# CS4102 Spring 2022 -- Unit D Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: hk4tnh
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import networkx

class TilingDino:
    def __init__(self):
        self.g = networkx.DiGraph()
        self.evens = []
        self.odds = []
        self.adj = []
        self.result = []
        self.counter = 0
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        width = len(lines[0])
        for j in range(0, len(lines)):
            for i in range(0, width):
                if lines[j][i] == "#":
                    self.counter += 1
                    n = node()
                    n.x = i
                    n.y = j
                    sum = j + i
                    if sum % 2 == 0:
                        self.evens.append(n)
                    else:
                        self.odds.append(n)
        #check if number of odds and evens are the same. if not, then it is not tile-able
        if len(self.evens) != len(self.odds):
            return ["impossible"]


        else:
            s = node()
            t = node()
            self.g.add_node(s)
            self.g.add_node(t)
            for x in self.evens:
                self.g.add_node(x)
                self.g.add_edge(s, x, capacity=1)
                for y in self.odds:
                    if not(self.g.has_node(y)):
                        self.g.add_node(y)
                        self.g.add_edge(y, t, capacity=1)
                    if self.checkIfAdj(x, y):
                        self.g.add_edge(x, y, capacity=1)


            pairings = networkx.maximum_flow(self.g, s, t)
            flow_dict = pairings[1]
            for a in flow_dict:
                if a != s and a != t:
                    for b in flow_dict[a]:
                        if b != s and b != t:
                            if flow_dict[a][b] == 1:
                                string = str(a.x) + " " + str(a.y) + " " + str(b.x) + " " + str(b.y)
                                self.result.append(string)
            if len(self.result) < (self.counter / 2):
                return ["impossible"]
            else:
                return self.result


    #find each #'s x and y's coordinates
    def checkIfAdj(self, node1, node2):
        if abs(node1.x - node2.x) == 1:
            if node1.y == node2.y:
                return True
            else:
                return False
        elif node1.x == node2.x:
            if abs(node1.y - node2.y) == 1:
                return True
            else:
                return False
        elif abs(node1.x - node2.x) > 1:
            return False
        elif abs(node1.y - node2.y) > 1:
            return False


class node:
    def __init__(self):
        self.x = 0
        self.y = 0

