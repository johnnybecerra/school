# Jhonatan Becerra
# wrestlers.py

import sys
import random

global nWrestlers
global nRivalries
nWrestlers = 0
nRivalries = 0

# returns a array with every line in the read file
# as input, it takes the name of a file
def readFile(fileName):
    # open a user defined file
    file = open(fileName, "r")

    # will store lines from the array
    fileLines = []

    # store every line
    for line in file:
        fileLines.append(line)

    return fileLines


# creates a graph with every wrestlers.
# takes as input an array with the lines read from the file
def processLines(fileLines):
    # first line will contain the number of wrestlers
    global nWrestlers
    global nRivalries
    nWrestlers = int(fileLines[0])
    nRivalries = int(fileLines[nWrestlers+1])

    # create graph to hold wrestlers
    wrestlers = Graph()

    # process wrestlers
    for w in range(1, nWrestlers +1):
        # create a wrestler Node from the file line
        wrestler = Node(fileLines[w].replace('\n',''))

        # add wrestler to wrestler graph
        wrestlers.addNode(wrestler)
    return wrestlers


# adds the desired rivalries to each given wrestler.
# as input, it takes the lines from the file
# and the graph of wrestlers
def addRivalries(fileLines, wrestlers):
    # process rivalries
    for r in range(nWrestlers +2, nWrestlers + nRivalries +2):
        # remove newline
        line = fileLines[r].replace('\n','')

        # split the string to simply wrestler names
        wName = line.split(" ")

        # add rivalries to each wrestler
        for wres in wName:
            for wres2 in wName:
                if wres != wres2:
                    wrestlers.addLinkToNode(wres, wres2)
    return wrestlers


# performs a breadth-first search for opposite types
# as input, it receives the graph and the
# starting node index
def wrestlerBFS(wGraph, sni):
    type1 = "Babyfaces"
    type2 = "Heels"

    # holds a queue for a BFS
    q = []

    # add first node to queue
    q.append(wGraph.node[sni])
    wGraph.node[sni].type = type1

    while q:
        # get the current node
        currentNode = q.pop(0)
        currentType = currentNode.type

        # process node
        # check adjoining node
        for adjNodeName in currentNode.nodeLink:
            adjNode = wGraph.getNode(adjNodeName)

            # check the type of the node
            if adjNode.type == "none":
                q.append(adjNode)

                # make child different type
                if currentType == type1:
                    adjNode.type = type2
                else:
                    adjNode.type = type1

            # child is already same type as parent
            elif adjNode.type == currentType:
                # if the child is the same type as the parent,
                # a rivarly is not possible
                return False

        # all connected nodes are done
        # check for unconnected nodes
        if len(q) == 0:
            # check if there are more that are unattached
            for i in wGraph.node:
                if i.type == "none":
                    q.append(i)
                    break

    # if search makes it to the end, rivalries are possible
    return True


# managing function
# pieces together all the different steps
def rivalries(fileName):
    # gets the lines from the file
    lines = readFile(fileName)

    # gets a graph with all wrestlers
    wGraph = processLines(lines)

    # adds rivalries to all wrestlers in graph
    wGraph = addRivalries(lines, wGraph)

    # perform a breadth-first search, with
    # a random wrestler as a starting point
    rp = wrestlerBFS(wGraph, random.randint(0, nWrestlers-1))

    # rivalry not possible
    if rp == False:
        print("Impossible")

    # rivalry possible
    else:
        print("Yes Possible")
        print("Babyfaces: {}".format(wGraph.printNodesOfType("Babyfaces")))
        print("Heels: {}".format(wGraph.printNodesOfType("Heels")))


# graph object will hold nodes
class Graph:
    def __init__(self):
        # array holding the nodes in the graph
        self.node = []

        # track number of nodes in the graph
        self.numNodes = 0

    # add a node to the graph
    def addNode(self, node):
        # add node to the array
        self.node.append(node)
        self.numNodes = self.numNodes + 1

    # searches for a node of name "name" in the graph
    # if it's found, returns its index in the array
    # returns -1 if it's not found
    def findNode(self, name):
        for i in range(0, self.numNodes):
            if self.node[i].name == name:
                return i
        return -1

    # returns a node with the name "name"
    def getNode(self, name):
        return self.node[self.findNode(name)]

    # finds a node of name "name" in the graph
    # and creates a directed edge to node named "link"
    def addLinkToNode(self, name, link):
        # search for node
        nodeIndex = self.findNode(name)

        # node was found
        if nodeIndex >= 0:
            # add the edges to the node
            self.node[nodeIndex].addLinkS(link)
        else:
            return

    # changes the type of a node
    def addTypeToNode(self, name, type):
        # search for the node
        nodeIndex = self.findNode(name)

        # node was found
        if nodeIndex >= 0:
            self.node[nodeIndex].changeType(type)

    # FOR TESTING:: prints all nodes in graph, along with their associations
    def printNodes(self):
        print("**********NODES IN GRAPH********")
        for n in range(0, self.numNodes):
            print("::Node {}:: {}".format(n+1, self.node[n].name))
            self.node[n].printNodeMeta()
        print("**********END NODES*************")

    # returns a string with  nodes that match the type "htype"
    def printNodesOfType(self, htype):
        ps = ""
        for g in self.node:
            if g.type == htype:
                ps = ps + g.name + " "
        return ps


# creates a node object which will represent every wrestler
class Node:
    # contructor
    def __init__(self, name):
        self.name = name
        self.nodeLink = []
        self.type = "none"

    def chageType(self, type):
        self.type = type

    def addLinkS(self, link):
        self.nodeLink.append(link)

    # FOR TESTING: prints all the links to other nodes
    def printLinks(self):
        # node has no links
        if len(self.nodeLink) < 1:
            print("{} :Node has no links".format(self.name))
            return

        # print links
        for node in self.nodeLink:
            print("---:LINK:- {}".format(node))

    # FOR TESTING: prints metadata about the node
    def printNodeMeta(self):
        print("*******NODE*******")
        print("Name: {}".format(self.name))
        print("Type: {}".format(self.type))
        self.printLinks()


if __name__ == "__main__":
    rivalries(sys.argv[1])