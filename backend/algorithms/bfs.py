from collections import deque


def bfs(graph, start, target):
    if start not in graph.routers:
        return {
            "found": False,
            "path": [],
            "hops": 0
        }

    if target not in graph.routers:
        return {
            "found": False,
            "path": [],
            "hops": 0
        }

    if graph.routers[start]["failed"]:
        return {
            "found": False,
            "path": [],
            "hops": 0
        }

    if graph.routers[target]["failed"]:
        return {
            "found": False,
            "path": [],
            "hops": 0
        }

    queue = deque([start])
    visited = {start}
    previous = {start: None}

    while queue:
        current = queue.popleft()

        if current == target:
            break

        for neighbor in graph.get_neighbors(current):
            next_router = neighbor["router"]

            if next_router not in visited:
                visited.add(next_router)
                previous[next_router] = current
                queue.append(next_router)

    if target not in visited:
        return {
            "found": False,
            "path": [],
            "hops": 0
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
        "hops": len(path) - 1
    }