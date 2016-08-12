#Graph code 3

from igraph import * #importing igraph library

g = Graph(3) #3 nodes

g.add_edge(0,1)
g.add_edge(1,2)

for i in range(0, g.vcount()): #g.vcount() counts t 
	print(g.degree(i))
	
summary(g) #print information about the g

plot(g, "code1.pdf")