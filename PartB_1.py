import heapq
class Intersection:
    def __init__(self, id):
        self.id = id

class Road:
    def __init__(self, id, name, length, start, end):
        self.id = id
        self.name = name #name of the road
        self.length = length #length of the road, which can represent distance or time
        self.start = start #intersection ID
        self.end = end #intersection ID

class TrafficGraph:
    def __init__(self, vertices):
        #creating a graph with 'vertices' number of vertices using a dictionary comprehension
        # where each vertex has a list to store its edges
        self.graph = {i: [] for i in range(vertices)}  #adjacency list representation

    def addRoad(self, road):
        self.graph[road.start].append((road.end, road.length))#edges from start to end with 'length' as the weight
        self.graph[road.end].append((road.start, road.length))#assuming undirected graph for bidirectional roads

    def dijkstra(self, start_vertex):
        #initialize distances from start_vertex to all others as infinity
        distances = {vertex: float('infinity') for vertex in self.graph} #minimum distances are initialized to infinity
        distances[start_vertex] = 0 # Distance to itself is 0
        priority_queue = [(0, start_vertex)] #priority queue to hold vertices and their current distances

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            # If a shorter path to the current vertex has been found previously, skip processing
            if current_distance > distances[current_vertex]:  #nodes can only be added once to the queue
                continue
                # Process each adjacent vertex
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                # If found path is shorter, update and push to the priority queue
                if distance < distances[neighbor]: #only consider this new path if it's better
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances #return the shortest paths from start_vertex to all other vertices

#example of using the graph
traffic_graph = TrafficGraph(100)  # max 100 vertices
#adding roads as edges to the graph
traffic_graph.addRoad(Road(1, "Main Street", 5, 0, 1))
traffic_graph.addRoad(Road(2, "Second Street", 3, 1, 2))
traffic_graph.addRoad(Road(3, "Third Avenue", 7, 0, 2))

#computing the shortest paths from vertex 0
shortest_paths = traffic_graph.dijkstra(0)
print("Shortest paths from intersection 0:", shortest_paths)
