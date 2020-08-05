# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:49:29 2020

@author: Admin
"""

import networkx as nx
import matplotlib.pyplot as plot



#using a random graph 
G=nx.gnp_random_graph(20,0.5)
#draw a graph 
nx.draw(G)

#showing a graph
plot.show()

# saving a file

nx.write_gexf(G,"networkxfile.gexf")

"""



22222





#showing a complete graph  bydefolut functoin using 
G=nx.complete_graph(10)
#draw a graph 
nx.draw(G)

#showing a graph
plot.show()

"""
'''


11111111 






#graf G is relate nx.Graph() class.
G =nx.Graph()
# node for tree 
G.add_node(1)
G.add_node(2)
G.add_node(3)

#edges for tree 
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)


#print nodes 
print(G.nodes())

#print edges 
print(G.edges())
 

#draw a graph 
nx.draw(G)

#showing a graph
plot.show()
'''