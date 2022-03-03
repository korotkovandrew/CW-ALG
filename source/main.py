# Python program for Bellman-Ford's single source 
# shortest path algorithm. 

from collections import defaultdict 
alphabet = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L"}

# Class to represent a graph 
class Graph: 

	def __init__(self, vertices): 
		self.V = vertices # No. of vertices 
		self.graph = [] # default dictionary to store graph 

	# function to add an edge to graph 
	def addEdge(self, u, v, w): 
		self.graph.append([u, v, w]) 
		
	# utility function used to print the solution 
	def printArr(self, dist): 
		print("Vertex Distance from Source")
		for i in range(self.V): 
			print("% s \t\t % d" % (alphabet[i], dist[i])) 
	
	# The main function that finds shortest distances from src to 
	# all other vertices using Bellman-Ford algorithm. The function 
	# also detects negative weight cycle 
	def BellmanFord(self, src): 

		# Step 1: Initialize distances from src to all other vertices 
		# as INFINITE 
		dist = [float("Inf")] * self.V 
		dist[src] = 0


		# Step 2: Relax all edges |V| - 1 times. A simple shortest 
		# path from src to any other vertex can have at-most |V| - 1 
		# edges 
		for i in range(self.V - 1): 
			print("Шаг: " + str(i))
			# Update dist value and parent index of the adjacent vertices of 
			# the picked vertex. Consider only those vertices which are still in 
			# queue 
			for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					uletter = alphabet[u]
					vletter = alphabet[v]
					dist[v] = dist[u] + w 
					print(vletter + ": " + str(dist[v]) + ", " + uletter)
						
		# print all distance 
		self.printArr(dist) 

g = Graph(12)


file = open("in.txt", mode="rt")

edges = file.read().split("/")
file.close()
for edge in edges:
	u = list(alphabet.keys())[list(alphabet.values()).index(edge[0])]
	v = list(alphabet.keys())[list(alphabet.values()).index(edge[1])]
	w = int(edge.split(" ")[1])
	g.addEdge(u, v, w)



# Print the solution 
g.BellmanFord(0) 
