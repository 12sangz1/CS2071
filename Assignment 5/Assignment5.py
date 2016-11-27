#Finding smallest connected spanning subgraph (spanning tree)

#Kruskall
	#iterate through edges and choose edges that do not form a cycle with already chosen edges

	#once all edges have been visited, the chosen edges form a spanning tree

	#procedure can be stopped as soon as number of chosen edges = numVertices - 1.

#Prim
	#initialize with V1 being any vertex in the graph (v), and E1 being empty
	
	#iterate numVertices-1 times
		#find cheapest edge (e) connecting a vertex in V to a vertex not in V1
		
		#Add new edge to E1, Add new vertex to V1
		
	