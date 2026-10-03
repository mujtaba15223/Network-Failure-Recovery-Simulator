import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
} from "reactflow";

import "reactflow/dist/style.css";

const positions = {
  R1: { x: 50, y: 100 },
  R2: { x: 300, y: 50 },
  R3: { x: 300, y: 200 },
  R4: { x: 550, y: 100 },
  R5: { x: 550, y: 300 },
  R6: { x: 800, y: 150 },
  R7: { x: 800, y: 350 },
  R8: { x: 1050, y: 250 },
};

const fallbackLinks = [
  ["R1", "R2"],
  ["R1", "R3"],
  ["R2", "R4"],
  ["R3", "R4"],
  ["R3", "R5"],
  ["R4", "R5"],
  ["R4", "R6"],
  ["R5", "R7"],
  ["R6", "R7"],
  ["R7", "R8"],
];

function NetworkGraph({ network, path = [] }) {
  const pathSet = new Set(path);
  const routePairs = new Set();

  for (let i = 0; i < path.length - 1; i += 1) {
    const pair = [path[i], path[i + 1]].sort().join("|");
    routePairs.add(pair);
  }

  const edgesData = Array.isArray(network?.links)
    ? network.links
    : Object.entries(network?.links || {}).flatMap(([from, neighbors]) =>
        (neighbors || []).map((link) => ({
          from,
          to: link.router,
          cost: link.cost,
          failed: !!link.failed,
        }))
      );

  const seenEdges = new Set();
  const edges = edgesData
    .filter(({ from, to }) => {
      const key = [from, to].sort().join("|");
      if (seenEdges.has(key)) return false;
      seenEdges.add(key);
      return true;
    })
    .map(({ from, to, cost, failed }) => {
      const routeActive = routePairs.has([from, to].sort().join("|"));

      return {
        id: `edge-${from}-${to}`,
        source: from,
        target: to,
        animated: routeActive,
        style: {
          stroke: failed ? "#ef4444" : routeActive ? "#22c55e" : "#a18c7a",
          strokeWidth: routeActive ? 4 : failed ? 2.5 : 2,
          strokeDasharray: failed ? "6 6" : undefined,
        },
        label: failed ? "down" : routeActive ? `${cost}` : undefined,
        labelStyle: {
          fill: routeActive ? "#86efac" : "#e7d8c8",
          fontSize: 11,
          fontWeight: 700,
        },
      };
    });

  const nodes = Object.entries(network.routers).map(([router, data]) => {
    const isRouteNode = pathSet.has(router);

    return {
      id: router,
      position: positions[router] || { x: 0, y: 0 },
      data: {
        label: `${router}${data.failed ? " (FAILED)" : ""}`,
      },
      style: {
        background: data.failed ? "#451a1a" : isRouteNode ? "#14532d" : "#2b211a",
        color: "#ffffff",
        border: data.failed
          ? "2px solid #ef4444"
          : isRouteNode
            ? "2px solid #22c55e"
            : "2px solid #a8794f",
        borderRadius: "10px",
        padding: "12px 18px",
        fontWeight: "bold",
        boxShadow: isRouteNode ? "0 0 12px rgba(34, 197, 94, 0.7)" : "none",
      },
    };
  });

  const finalEdges = edges.length > 0 ? edges : fallbackLinks.map(([from, to], index) => {
    const routeActive = routePairs.has([from, to].sort().join("|"));

    return {
      id: `edge-${index}`,
      source: from,
      target: to,
      animated: routeActive,
      style: {
        stroke: routeActive ? "#22c55e" : "#9b826b",
        strokeWidth: routeActive ? 4 : 2,
      },
    };
  });

  return (
    <div className="network-graph">
      <ReactFlow
        nodes={nodes}
        edges={finalEdges}
        fitView
        nodesDraggable={false}
        nodesConnectable={false}
      >
        <Background />
        <Controls />
        <MiniMap />
      </ReactFlow>
    </div>
  );
}

export default NetworkGraph;