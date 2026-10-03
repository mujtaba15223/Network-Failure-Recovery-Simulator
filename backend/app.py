from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from models.graph import Graph
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.connected_components import connected_components
from algorithms.critical_connections import find_critical_connections


app = Flask(__name__)

CORS(app)


def create_graph():
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

    return graph


graph = create_graph()


@app.route("/")
def home():
    return jsonify({
        "name": "NetworkGuard API",
        "status": "running"
    })


@app.route("/api/network")
def network():
    components = connected_components(graph)

    return jsonify({
        "routers": graph.routers,
        "links": {
            router: [
                {
                    "router": link["router"],
                    "cost": link["cost"],
                    "failed": link["failed"]
                }
                for link in neighbors
            ]
            for router, neighbors in graph.links.items()
        },
        "components": components,
        "component_count": len(components)
    })


@app.route("/api/bfs")
def run_bfs():
    start = request.args.get("start")
    target = request.args.get("target")

    if not start or not target:
        return jsonify({
            "error": "start and target are required"
        }), 400

    result = bfs(graph, start, target)

    return jsonify(result)


@app.route("/api/dfs")
def run_dfs():
    start = request.args.get("start")

    if not start:
        return jsonify({
            "error": "start is required"
        }), 400

    result = dfs(graph, start)

    return jsonify(result)


@app.route("/api/dijkstra")
def run_dijkstra():
    start = request.args.get("start")
    target = request.args.get("target")

    if not start or not target:
        return jsonify({
            "error": "start and target are required"
        }), 400

    result = dijkstra(graph, start, target)

    return jsonify(result)


@app.route("/api/connected-components")
def run_connected_components():
    components = connected_components(graph)

    return jsonify({
        "components": components,
        "count": len(components)
    })


@app.route("/api/critical-connections")
def critical_connections():
    result = find_critical_connections(graph)

    return jsonify({
        "critical_connections": result,
        "count": len(result)
    })


@app.route("/api/failure/router", methods=["POST"])
def fail_router():
    data = request.get_json(silent=True) or {}

    router_id = data.get("router")

    if not router_id:
        return jsonify({
            "error": "router is required"
        }), 400

    if router_id not in graph.routers:
        return jsonify({
            "error": "router not found"
        }), 404

    graph.fail_router(router_id)

    return jsonify({
        "message": f"Router {router_id} failed",
        "router": router_id
    })


@app.route("/api/restore/router", methods=["POST"])
def restore_router():
    data = request.get_json(silent=True) or {}

    router_id = data.get("router")

    if not router_id:
        return jsonify({
            "error": "router is required"
        }), 400

    if router_id not in graph.routers:
        return jsonify({
            "error": "router not found"
        }), 404

    graph.restore_router(router_id)

    return jsonify({
        "message": f"Router {router_id} restored",
        "router": router_id
    })


@app.route("/api/failure/link", methods=["POST"])
def fail_link():
    data = request.get_json(silent=True) or {}

    router1 = data.get("from")
    router2 = data.get("to")

    if not router1 or not router2:
        return jsonify({
            "error": "from and to are required"
        }), 400

    if router1 not in graph.routers or router2 not in graph.routers:
        return jsonify({
            "error": "router not found"
        }), 404

    graph.fail_link(router1, router2)

    return jsonify({
        "message": f"Link {router1} - {router2} failed",
        "from": router1,
        "to": router2
    })


@app.route("/api/restore/link", methods=["POST"])
def restore_link():
    data = request.get_json(silent=True) or {}

    router1 = data.get("from")
    router2 = data.get("to")

    if not router1 or not router2:
        return jsonify({
            "error": "from and to are required"
        }), 400

    if router1 not in graph.routers or router2 not in graph.routers:
        return jsonify({
            "error": "router not found"
        }), 404

    graph.restore_link(router1, router2)

    return jsonify({
        "message": f"Link {router1} - {router2} restored",
        "from": router1,
        "to": router2
    })


@app.route("/api/reset", methods=["POST"])
def reset_network():
    global graph

    graph = create_graph()

    return jsonify({
        "message": "Network reset successfully"
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )