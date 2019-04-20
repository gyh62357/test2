# -*- coding: utf-8 -*-
# @File  : map.py
# @Author: 郭迎辉
# @Time  : 2018/12/6/00612:40
# @Desc  :
from networkx import read_edgelist
import matplotlib.pyplot as plt
import networkx as nx
G = read_edgelist('E:/edge.edgelist')
print(G.number_of_nodes())
nx.draw(G)
plt.show()



