import json

from models.graph import Graph
from algorithms.connected_components import connected_components
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra


graph = Graph()

with open("data/sample_network.json") as file:
    data = json.load(file)

for router in data["routers"]:
    graph.add_router(router)

for link in data["links"]:
    graph.add_link(
        link["from"],
        link["to"],
        link["cost"]
    )


print("Original network:")
print(connected_components(graph))


print("\nBFS: R1 to R8")

result = bfs(graph, "R1", "R8")

print("Found:", result["found"])
print("Path:", result["path"])
print("Hops:", result["hops"])


print("\nDFS: Starting from R1")

result = dfs(graph, "R1")

print("Found:", result["found"])
print("Traversal:", result["order"])


print("\nDijkstra: R1 to R8")

result = dijkstra(graph, "R1", "R8")

print("Found:", result["found"])
print("Path:", result["path"])
print("Cost:", result["cost"])


print("\nFailing R4...")

graph.fail_router("R4")

print("After failure:")
print(connected_components(graph))


print("\nBFS after R4 failure: R1 to R8")

result = bfs(graph, "R1", "R8")

print("Found:", result["found"])
print("Path:", result["path"])
print("Hops:", result["hops"])


print("\nDFS after R4 failure: Starting from R1")

result = dfs(graph, "R1")

print("Found:", result["found"])
print("Traversal:", result["order"])


print("\nDijkstra after R4 failure: R1 to R8")

result = dijkstra(graph, "R1", "R8")

print("Found:", result["found"])
print("Path:", result["path"])
print("Cost:", result["cost"])