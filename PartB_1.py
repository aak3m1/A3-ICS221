import heapq

class Intersection:
    def __init__(self, id):
        self.id = id

class Road:
    def __init__(self, id, name, length, start, end):
        self.id = id
        self.name = name
        self.length = length
        self.start = start
        self.end = end

class TrafficGraph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}  # adjacency list representation

    def add_road(self, road):
        # Edge from start to end with 'length' as the weight
        self.graph[road.start].append((road.end, road.length))
        # Assuming undirected graph for bidirectional roads
        self.graph[road.end].append((road.start, road.length))

    def dijkstra(self, start_vertex):
        # Minimum distances are initialized to infinity
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        # Priority queue to hold vertices and their current distances
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Nodes can only be added once to the queue
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example of using the graph
traffic_graph = TrafficGraph(100)  # max 100 vertices
traffic_graph.add_road(Road(1, "Main Street", 5, 0, 1))
traffic_graph.add_road(Road(2, "Second Street", 3, 1, 2))
traffic_graph.add_road(Road(3, "Third Avenue", 7, 0, 2))

# Compute shortest paths from vertex 0
shortest_paths = traffic_graph.dijkstra(0)
print("Shortest paths from intersection 0:", shortest_paths)
