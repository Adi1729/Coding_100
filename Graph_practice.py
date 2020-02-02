# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:53:58 2018

@author: aditya
"""
g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }
    
class Graph(object):
    def __init__(self,graph):
        self.graph = graph
        print(graph)
         
            
    def vertices(self):
        vertex=[]
        for node in self.graph.keys():
            vertex.append(node)
        return vertex
            
    def edges(self):
        edge=[]
        for node in self.graph.keys():
            for neighbour in self.graph[node]:
                edge.append((node,neighbour))
                
        return edge
        
    def add_vertex(self,v1):
        return self.graph.update(v1)
        
    
    def add_edge(self,edge,v1):
        for neighbour in self.graph[v1]:
            edge.append((v1,neighbour))
        return edge
        
    
graph1 = Graph(g)

print("Vertices of graph:")
print(graph1.vertices())

print("Edges of graph:")
print(graph1.edges())

print("Add vertex:")
graph1.add_vertex("z")

print("Vertices of graph:")
print(graph1.vertices())
 
print("Add an edge:")
graph1.add_edge({"a","z"})

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})
print("Vertices of graph:")
print(graph.vertices())
print("Edges of graph:")
print(graph.edges())
  
    
