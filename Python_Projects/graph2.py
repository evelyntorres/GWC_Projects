#Graph code 2

from igraph import * #importing igraph library

g = Graph(3) #3 nodes

for i in range(0, g.vcount()): #g.vcount() counts t 
	print(g.degree(i))
	
summary(g) #print information about the g

plot(g, "code1.pdf")