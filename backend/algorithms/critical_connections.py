from algorithms.connected_components import connected_components


def find_critical_connections(graph):
    critical = []

    for router1 in graph.routers:

        if graph.routers[router1]["failed"]:
            continue

        for link in graph.links.get(router1, []):

            router2 = link["router"]

            if router1 >= router2:
                continue

            if graph.routers[router2]["failed"]:
                continue

            if link["failed"]:
                continue

            original_components = len(
                connected_components(graph)
            )

            graph.fail_link(router1, router2)

            new_components = len(
                connected_components(graph)
            )

            graph.restore_link(router1, router2)

            if new_components > original_components:
                critical.append({
                    "from": router1,
                    "to": router2,
                    "impact": new_components - original_components
                })

    return critical