#Graph code 4

from igraph import * #importing igraph library

g = Graph.Read_Ncol("code4.txt", directed=False)



for i in range(0, g.vcount()): #g.vcount() counts t 
	print(g.degree(i))
	
summary(g) #print information about the g

plot(g, "code4.pdf")