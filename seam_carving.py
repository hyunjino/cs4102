# CS4102 Spring 2022 -- Unit C Programming
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
import math
import sys


class SeamCarving:
    def __init__(self):
        self.h = 0
        self.w = 0
        self.seam = []
        self.minIndex = 0
        self.memTable = []
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    #
    # @return the seam's weight
    def run(self, image):
        h = len(image)
        w = len(image[0])
        self.h = h
        self.w = w
        energyTable = [[0.0 for x in image[0]] for y in image]
        memTable = [[0.0 for x in image[0]] for y in image]
        self.memTable = memTable

        for j in range(0, h):
            for i in range(0, w):
                energyTable[j][i] = self.getEnergy(j, i, image)
                memTable[j][i] = self.getEnergy(j, i, image)

        # filling out memTable frm bottom to top
        for j in range(h - 1, -1, -1):
            for i in range(0, w):
                #initialize bottom row
                if j == h - 1:
                    memTable[j][i] = energyTable[j][i]
                #check if on left edge
                elif i == 0:
                    memTable[j][i] = energyTable[j][i] + min(memTable[j + 1][i], memTable[j + 1][i + 1])
                elif i == w - 1:
                    memTable[j][i] = energyTable[j][i] + min(memTable[j + 1][i - 1], memTable[j + 1][i])
                else:
                    memTable[j][i] = energyTable[j][i] + min(memTable[j + 1][i - 1], memTable[j + 1][i], memTable[j + 1][i + 1])

        #finding the min energy pixel at the top row

        minEnergy = 1000000
        for i in range(0, self.w):
            if memTable[0][i] <= minEnergy:
                minEnergy = memTable[0][i]
                self.minIndex = i

        #for j in range(0, h - 1):
        #    x = self.getNextElement(j, self.minIndex, memTable)
        #    self.seam.append(x)
        #    self.minIndex = self.getNextElement(j, x, memTable)

        return minEnergy

    def getNextElement(self, j, i, memTable):
        k = i
        if i == 0:
            if memTable[j + 1][i] > memTable[j + 1][i + 1]:
                k = i + 1
        elif i == self.w - 1:
            if memTable[j + 1][i - 1] < memTable[j + 1][i]:
                k = i - 1
        else:
            if memTable[j + 1][i - 1] < memTable[j + 1][i] and memTable[j + 1][i - 1] < memTable[j + 1][i + 1]:
                k = i - 1
            elif memTable[j + 1][i + 1] < memTable[j + 1][i] and memTable[j + 1][i + 1] < memTable[j + 1][i - 1]:
                k = i + 1
        return k


    def getEnergy(self, j, i, image):
        neighbors = 0.0
        sum = 0.0
        for y in range (j-1, j+2):
            for x in range (i-1, i+2):
                if 0<= x <= self.w - 1 and 0<= y <= self.h -1:
                    neighbors += 1.0
                    sum += math.sqrt(((image[j][i][0] - image[y][x][0])**2) + ((image[j][i][2] - image[y][x][2])**2) + ((image[j][i][1] - image[y][x][1])**2))
        return sum/(neighbors - 1)

    def getDistance(self, p1, p2):
        return math.sqrt(((p2[0] - p1[0])**2) + ((p2[2] - p1[2])**2) + ((p2[1] - p1[1])**2))

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    #
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    #
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array

    def getSeam(self):
        k = self.minIndex
        self.seam.append(k)
        for j in range(self.h-1):
            if k == 0:
                if self.memTable[j + 1][k] > self.memTable[j + 1][k + 1]:
                    k = k + 1
            elif k == self.w - 1:
                if self.memTable[j + 1][k - 1] < self.memTable[j + 1][k]:
                    k = k - 1
            else:
                if self.memTable[j + 1][k - 1] < self.memTable[j + 1][k] and self.memTable[j + 1][k - 1] < self.memTable[j + 1][k + 1]:
                    k = k - 1
                elif self.memTable[j + 1][k + 1] < self.memTable[j + 1][k] and self.memTable[j + 1][k + 1] < self.memTable[j + 1][k - 1]:
                    k = k + 1
            self.seam.append(k)
        return self.seam


