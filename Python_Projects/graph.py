#Graph code 1

from igraph import * #importing igraph library

g = Graph(3) #3 nodes

summary(g) #print information about the g

plot(g, "code1.pdf")