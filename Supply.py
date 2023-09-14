# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: hk4tnh
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################

class Supply:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        temp = file_data[0]
        temp2 = temp.split(" ")
        numNodes = int(temp2[0])
        numCons = int(temp2[1])

        nodeTypes = {}
        disjointSet = {}
        connections = []
        validConnections = []

        stores  = {}

        for i in range(1, numNodes +1):
            temp3 = file_data[i]
            temp4 = temp3.split(" ")
            nodeTypes[temp4[0]] = temp4[1]

        for i in range(numNodes+1, numNodes+numCons+1):
            temp5 = file_data[i]
            temp6 = temp5.split(" ")
            connections.append(temp6)

        sortedConnections = self.insertSort(connections)


        for i in sortedConnections:
            if nodeTypes[i[0]] == "store":
                stores[i[0]] = 0
            if nodeTypes[i[1]] == "store":
                stores[i[1]] = 0
            if self.checkValid(i[0], i[1], stores, nodeTypes):
                validConnections.append(i)





        edgeWeightSum = 0

        #making the disjoinSet where each node is its own parent
        for i in validConnections:
            disjointSet[i[0]] = i[0]
            disjointSet[i[1]] = i[1]

        for i in validConnections:
            node1 = i[0]
            node2 = i[1]
            if checkIfSameTree(node1, node2, disjointSet) == False:
                edgeWeightSum += int(i[2])
                union(node1, node2, disjointSet)

        # your function to compute the result should be called here

        return edgeWeightSum


    def checkValid(self, node1, node2, stores, dict):
        if dict[node1] == "port":
            if dict[node2] == "store":
                return False
            else:
                return True

        if dict[node1] == "rail-hub":
            if dict[node2] == "store":
                return False
            else:
                return True

        if dict[node1] == "dist-center":
            if dict[node2] == "dist-center":
                return False
            if dict[node2] == "store":
                if stores[node2] == 0:
                    stores[node2] = node1
                    return True
                else:
                    return False
            else:
                return True

        if dict[node1] == "store":
            if dict[node2] == "rail-hub":
                return False
            if dict[node2] == "port":
                return False
            if dict[node2] == "dist-center":
                if stores[node1] == 0:
                    stores[node1] = node2
                    return True
                else:
                    return False
            else:
                return True



    def insertSort(self, listoflists):
        for i in range(1, len(listoflists)):
            key = listoflists[i]
            keyValue = int(key[2])
            j = i - 1

            # Compare key with each element on the left of it until an element smaller than it is found
            # For descending order, change key<array[j] to key>array[j].
            while j >= 0 and keyValue < int(listoflists[j][2]):
                listoflists[j + 1] = listoflists[j]
                j = j - 1

            # Place key at after the element just smaller than it.
            listoflists[j + 1] = key
        return listoflists




def findRoot(node, set):
    x = set[node]
    if x == node:
        return x
    else:
        return findRoot(x, set)

def union(node1, node2, set):
    parent1 = findRoot(node1, set)
    parent2 = findRoot(node2, set)
    set[parent1] = parent2

def checkIfSameTree(node1, node2, set):
    if findRoot(node1, set) != findRoot(node2, set):
        return False
    else: return True

