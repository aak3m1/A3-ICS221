import heapq

class TrafficGraph:
    def __init__(self, vertices):
        #creating a graph with 'vertices' number of vertices
        #graph is represented as an adjacency list
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, start, end, length):
        self.graph[start].append((end, length)) #adding an edge to the graph from 'start' to 'end' with a weight of 'length'
        self.graph[end].append((start, length)) #add the reverse edge as well

    def dijkstra(self, start_vertex, target_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph} #all distances as infinity
        distances[start_vertex] = 0 #distance from the start vertex to itself is zero
        priority_queue = [(0, start_vertex)] #piority queue for maintaining vertices to visit

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)#pop the vertex with the smallest distance from the start vertex
            if current_vertex == target_vertex: #if the target vertex is reached, exit the loop
                break  # Stop if the target is reached

            if current_distance > distances[current_vertex]:#if  current distance is greater than the known distance
                continue

            for neighbor, weight in self.graph[current_vertex]: #check all adjacent vertices (neighbors)
                distance = current_distance + weight #distance through the current vertex to the neighbor

                if distance < distances[neighbor]: #if the new distance is shorter
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor)) #update the distance and add the neighbor to the queue
        return distances[target_vertex] #return the shortest distance to the target vertex

graph = TrafficGraph(vertices=10) #graph instance with 10 vertices

#edges between vertices with their respective weights
graph.add_edge(0, 1, 4)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 4, 1)
graph.add_edge(1, 5, 7)
graph.add_edge(5, 6, 3)
graph.add_edge(6, 4, 2)

#finding the shortest path from point A (0) to point B (4)
shortest_distance = graph.dijkstra(start_vertex=0, target_vertex=4)
print(f"The shortest distance from point A to point B is: {shortest_distance}")
