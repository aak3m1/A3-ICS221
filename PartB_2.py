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

    def add_road(self, road):
        self.graph[road.start].append((road.end, road.length)) #edges from start to end with 'length' as the weight
        self.graph[road.end].append((road.start, road.length)) #assuming undirected graph for bidirectional roads
        print(f"Road added between {road.start} and {road.end} with length {road.length}")

    def dijkstra(self, start_vertex):
        #initialize distances from start_vertex to all others as infinity
        distances = {vertex: float('infinity') for vertex in self.graph}  #minimum distances are initialized to infinity
        distances[start_vertex] = 0 #distance to itself is 0
        priority_queue = [(0, start_vertex)] #priority queue to hold vertices and their current distances
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue  #skip if a shorter path to current_vertex has already been processed
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:  #check if a shorter path to 'neighbor' is found
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances  #return the computed shortest path distances

class House:
    def __init__(self, id, address):
        self.id = id  # Unique identifier for the house
        self.address = address  # Physical address of the house

class PackageDistributionGraph(TrafficGraph):
    def __init__(self, vertices):
        super().__init__(vertices)  #initialize the base TrafficGraph with specified number of vertices
        self.houses = {}  #dictionary to store house objects

    def add_house(self, house, intersection_id):
        self.houses[house.id] = house
        #connect house to intersection with minimal impact on traffic (e.g., weight 0.1 for road length)
        self.add_road(Road(house.id, f"Access to {house.address}", 0.1, house.id, intersection_id))

    def distribute_packages(self, warehouse_id):
        print(f"Distributing packages from warehouse at intersection {warehouse_id}")
        distances = self.dijkstra(warehouse_id)  #using the Dijkstra's algorithm to find shortest paths from warehouse
        return distances

    def print_reachable_routes(self, package_routes):
        print("")
        print("Package delivery routes from warehouse:")
        for key, value in package_routes.items():
            if value < float('infinity'):  #only print reachable destinations
                if key in self.houses:  #checking if the destination is a house
                    print(f"House {self.houses[key].address} at {key}: {value} min")
                else:
                    print(f"Intersection {key}: {value} min")


distribution_graph = PackageDistributionGraph(100)
distribution_graph.add_road(Road(1, "Al Maktoum Airport Street", 5, 0, 1))
distribution_graph.add_road(Road(2, "Al Yalayis Street", 3, 1, 2))
distribution_graph.add_road(Road(3, "Hessa Street", 7, 0, 2))

distribution_graph.add_house(House(4, "889 Al Maktoum Airport Street"), 1)
distribution_graph.add_house(House(5, "112 Al Yalayis Street"), 2)

package_routes = distribution_graph.distribute_packages(0)
distribution_graph.print_reachable_routes(package_routes)