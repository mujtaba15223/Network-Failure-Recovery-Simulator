def connected_components(graph):
    visited = set()
    components = []

    for router in graph.routers:

        if router in visited:
            continue

        if graph.routers[router]["failed"]:
            continue

        component = []
        stack = [router]

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            if graph.routers[current]["failed"]:
                continue

            visited.add(current)
            component.append(current)

            for neighbor in graph.get_neighbors(current):
                next_router = neighbor["router"]

                if next_router not in visited:
                    stack.append(next_router)

        components.append(component)

    return components