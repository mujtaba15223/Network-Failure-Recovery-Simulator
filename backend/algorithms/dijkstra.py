import heapq


def dijkstra(graph, start, target):
    if start not in graph.routers:
        return {
            "found": False,
            "path": [],
            "cost": 0
        }

    if target not in graph.routers:
        return {
            "found": False,
            "path": [],
            "cost": 0
        }

    if graph.routers[start]["failed"]:
        return {
            "found": False,
            "path": [],
            "cost": 0
        }

    if graph.routers[target]["failed"]:
        return {
            "found": False,
            "path": [],
            "cost": 0
        }

    distances = {
        router: float("inf")
        for router in graph.routers
    }

    previous = {
        router: None
        for router in graph.routers
    }

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_cost, current = heapq.heappop(priority_queue)

        if current_cost > distances[current]:
            continue

        if current == target:
            break

        for neighbor in graph.get_neighbors(current):
            next_router = neighbor["router"]
            edge_cost = neighbor["cost"]

            new_cost = current_cost + edge_cost

            if new_cost < distances[next_router]:
                distances[next_router] = new_cost
                previous[next_router] = current

                heapq.heappush(
                    priority_queue,
                    (new_cost, next_router)
                )

    if distances[target] == float("inf"):
        return {
            "found": False,
            "path": [],
            "cost": 0
        }

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return {
        "found": True,
        "path": path,
        "cost": distances[target]
    }