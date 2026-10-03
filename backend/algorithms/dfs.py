def dfs(graph, start):
    if start not in graph.routers:
        return {
            "found": False,
            "order": []
        }

    if graph.routers[start]["failed"]:
        return {
            "found": False,
            "order": []
        }

    visited = set()
    order = []

    def visit(router):
        if router in visited:
            return

        if graph.routers[router]["failed"]:
            return

        visited.add(router)
        order.append(router)

        for neighbor in graph.get_neighbors(router):
            next_router = neighbor["router"]

            if next_router not in visited:
                visit(next_router)

    visit(start)

    return {
        "found": True,
        "order": order
    }