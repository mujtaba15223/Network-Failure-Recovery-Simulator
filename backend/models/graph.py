class Graph:
    def __init__(self):
        self.routers = {}
        self.links = {}

    # Add a router
    def add_router(self, router_id):
        if router_id not in self.routers:
            self.routers[router_id] = {
                "failed": False
            }

    # Add a network link
    def add_link(self, router1, router2, cost):
        self.add_router(router1)
        self.add_router(router2)

        self.links.setdefault(router1, []).append({
            "router": router2,
            "cost": cost,
            "failed": False
        })

        self.links.setdefault(router2, []).append({
            "router": router1,
            "cost": cost,
            "failed": False
        })

    # Fail a router
    def fail_router(self, router_id):
        if router_id in self.routers:
            self.routers[router_id]["failed"] = True

    # Restore a router
    def restore_router(self, router_id):
        if router_id in self.routers:
            self.routers[router_id]["failed"] = False

    # Fail a link
    def fail_link(self, router1, router2):
        for link in self.links.get(router1, []):
            if link["router"] == router2:
                link["failed"] = True

        for link in self.links.get(router2, []):
            if link["router"] == router1:
                link["failed"] = True

    # Restore a link
    def restore_link(self, router1, router2):
        for link in self.links.get(router1, []):
            if link["router"] == router2:
                link["failed"] = False

        for link in self.links.get(router2, []):
            if link["router"] == router1:
                link["failed"] = False

    # Get active neighbors
    def get_neighbors(self, router_id):
        if router_id not in self.routers:
            return []

        if self.routers[router_id]["failed"]:
            return []

        neighbors = []

        for link in self.links.get(router_id, []):
            neighbor = link["router"]

            if self.routers[neighbor]["failed"]:
                continue

            if link["failed"]:
                continue

            neighbors.append({
                "router": neighbor,
                "cost": link["cost"]
            })

        return neighbors