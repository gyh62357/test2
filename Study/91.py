# -*- coding: utf-8 -*-
# @File  : 91.py
# @Author: 郭迎辉
# @Time  : 2019/3/13/01315:31
# @Desc  :
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
H = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(range(4,7))
H.add_node(7)
G.add_nodes_from(H)

G.add_edge(1,2)
G.add_edge(1,1)
G.add_edges_from([(2,3),(3,6),(4,6),(5,6)])
H.add_edges_from([(4,7),(5,7),(6,7)])
G.add_edges_from(H.edges())

nx.draw_networkx(G)
plt.show()