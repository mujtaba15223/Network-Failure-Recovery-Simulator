# 🛡️ NetworkGuard — Network Failure Recovery Simulator

NetworkGuard is an interactive network failure recovery simulator designed to analyze network topology, simulate router and link failures, identify disconnected components, find alternate routes, and detect critical connections.

The system demonstrates important **Design and Analysis of Algorithms (DAA)** concepts through a visual web-based dashboard.

---

## 🚀 Features

- 🌐 Interactive network topology visualization
- 🖥️ Router status monitoring
- ❌ Simulate router failures
- 🔗 Simulate network link failures
- 🔄 Restore failed routers and links
- 🧩 Detect disconnected network components
- 🛣️ Find alternate routes using BFS
- ⚡ Find lowest-cost routes using Dijkstra
- 🔍 Network traversal using DFS
- 🚨 Identify critical network connections
- 📊 Display network statistics
- 🔄 Reset the network to its original state
- 🎯 Interactive algorithm results
- 📱 Responsive dashboard interface

---

## 🧠 Algorithms Used

### 1. Breadth-First Search (BFS)

BFS explores the network level by level.

In NetworkGuard, BFS is used to:

- Find minimum-hop routes
- Check network reachability
- Discover alternate paths after failures

Example:

```text
R1 → R3 → R5 → R7 → R8
```

---

### 2. Depth-First Search (DFS)

DFS explores the network deeply before backtracking.

It is used for:

- Network traversal
- Reachability analysis
- Structural exploration of the network

---

### 3. Dijkstra's Algorithm

Dijkstra's algorithm finds the lowest-cost route between two routers when link costs are non-negative.

NetworkGuard uses it to determine:

- Lowest-cost recovery routes
- Optimal paths after failures
- Total recovery cost

Example:

```text
R1 → R3 → R4 → R5 → R7 → R8
```

---

### 4. Connected Components

Connected Components analysis identifies groups of routers that remain mutually reachable.

It is used to:

- Detect network fragmentation
- Determine disconnected regions
- Measure the impact of failures

---

### 5. Critical Connection Analysis

NetworkGuard analyzes network links by simulating their failure and checking whether the number of connected components increases.

This helps identify connections whose failure can cause network fragmentation.

---

## 🏗️ System Architecture

```text
                    NetworkGuard
                         │
              ┌──────────┴──────────┐
              │                     │
          React Frontend        Flask Backend
              │                     │
       Interactive Dashboard    REST API
              │                     │
              └──────────┬──────────┘
                         │
                    Graph Model
                         │
        ┌────────────────┼────────────────┐
        │        │       │       │        │
       BFS      DFS  Dijkstra   CC   Critical Links
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend | Python |
| API | Flask |
| CORS | Flask-CORS |
| HTTP Client | Axios |
| Graph Visualization | React Flow |
| Icons | Lucide React |
| Algorithms | BFS, DFS, Dijkstra, Connected Components |
| Data | JSON |
| Package Manager | npm |
| Version Control | Git |

---

## 📁 Project Structure

```text
network-failure-recovery/
│
├── backend/
│   │
│   ├── algorithms/
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── dijkstra.py
│   │   ├── connected_components.py
│   │   └── critical_connections.py
│   │
│   ├── models/
│   │   └── graph.py
│   │
│   ├── data/
│   │   └── sample_network.json
│   │
│   ├── app.py
│   └── test_graph.py
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   └── NetworkGraph.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

## 🌐 Sample Network

The simulator contains 8 routers:

```text
R1
R2
R3
R4
R5
R6
R7
R8
```

Example network connections:

```text
R1 ── R2
│
└── R3 ── R4 ── R6
     │    │      │
     │    └──────┘
     │
     └── R5 ── R7 ── R8
```

Each network link has an associated cost used by Dijkstra's algorithm.

---

## 🔌 REST API

### Health Check

```http
GET /
```

Returns:

```json
{
  "name": "NetworkGuard API",
  "status": "running"
}
```

---

### Get Network

```http
GET /api/network
```

Returns routers, connected components, component count, and failed links.

---

### BFS

```http
GET /api/bfs?start=R1&target=R8
```

Returns the minimum-hop route.

---

### DFS

```http
GET /api/dfs?start=R1
```

Returns the DFS traversal order.

---

### Dijkstra

```http
GET /api/dijkstra?start=R1&target=R8
```

Returns the lowest-cost route.

---

### Connected Components

```http
GET /api/connected-components
```

Returns the current network components.

---

### Critical Connections

```http
GET /api/critical-connections
```

Returns connections whose failure increases network fragmentation.

---

### Fail Router

```http
POST /api/failure/router
```

Request:

```json
{
  "router": "R4"
}
```

---

### Restore Router

```http
POST /api/restore/router
```

Request:

```json
{
  "router": "R4"
}
```

---

### Fail Link

```http
POST /api/failure/link
```

Request:

```json
{
  "from": "R1",
  "to": "R3"
}
```

---

### Restore Link

```http
POST /api/restore/link
```

Request:

```json
{
  "from": "R1",
  "to": "R3"
}
```

---

### Reset Network

```http
POST /api/reset
```

Restores the complete network to its initial state.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/network-failure-recovery.git
```

```bash
cd network-failure-recovery
```

---

## 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask flask-cors
```

Start the backend:

```bash
python app.py
```

Backend will run at:

```text
http://localhost:5000
```

---

## ⚛️ Frontend Setup

Open another terminal and navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at the URL shown by Vite, typically:

```text
http://localhost:5173
```

---

## 🎮 How to Use

### Step 1 — Open Dashboard

Open the React frontend in your browser.

### Step 2 — View Network

The dashboard displays the complete network topology.

### Step 3 — Simulate Router Failure

Click **Fail** on any active router.

The dashboard updates the router status and network components.

### Step 4 — Simulate Link Failure

Use the **Link Failure Simulation** section to fail a network connection.

Failed connections are displayed differently on the network graph.

### Step 5 — Find an Alternate Route

Select:

```text
Start Router
Target Router
Algorithm
```

Then click:

```text
Run Algorithm
```

### Step 6 — Analyze Critical Connections

The **Critical Connections** section identifies connections whose failure increases network fragmentation.

### Step 7 — Restore Network

Individual routers/links can be restored, or the complete network can be reset using:

```text
Reset Network
```

---

## 📊 Example Algorithm Results

### BFS

```text
Start: R1
Target: R8

Path:
R1 → R3 → R5 → R7 → R8

Minimum Hops:
4
```

### Dijkstra

```text
Start: R1
Target: R8

Path:
R1 → R3 → R4 → R5 → R7 → R8

Total Cost:
11
```

After a router failure, Dijkstra can select a different available path based on the remaining network topology.

---

## 🎯 Problem Statement

**Problem 55 — Network Failure Recovery Simulator**

The system models routers and network links as a graph and simulates failures to identify:

- Disconnected components
- Alternate routes
- Critical connections

The project demonstrates how graph algorithms can support network failure analysis and recovery decisions.

---

## 🎓 DAA Concepts Demonstrated

This project demonstrates:

- Graph representation
- Graph traversal
- Breadth-First Search
- Depth-First Search
- Shortest path algorithms
- Connected components
- Weighted graphs
- Failure simulation
- Path reconstruction
- Network recovery analysis
- Algorithmic decision making

---

## 🔮 Future Enhancements

Possible future improvements include:

- Real-time network monitoring
- User-created network topologies
- Custom router and link creation
- Network performance metrics
- More advanced critical-link analysis
- Algorithm animation
- Failure history and recovery logs
- Authentication
- Persistent database storage
- Production deployment
- Network traffic simulation

---

## 👨‍💻 Author

**Mohd Mujtaba**

B.Tech Computer Science & Engineering  
Specialization: Artificial Intelligence & Machine Learning

---

## 📜 License

This project is developed for educational, demonstration, and hackathon purposes.
