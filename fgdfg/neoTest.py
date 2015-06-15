__author__ = 'SU915198'
from py2neo import Node, Rel, Graph


# node_name = Node("http://localhost:7474/db/data")

graph = Graph("http://localhost:7474/")

n = graph.node("People")
