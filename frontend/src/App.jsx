import { useEffect, useState } from "react";
import axios from "axios";
import {
  Activity,
  Network,
  Server,
  AlertTriangle,
  RotateCcw,
  Route,
} from "lucide-react";

import NetworkGraph from "./components/NetworkGraph";
import "./App.css";

const API = "http://localhost:5000";

function App() {
  const [network, setNetwork] = useState(null);
  const [start, setStart] = useState("R1");
  const [target, setTarget] = useState("R8");
  const [algorithm, setAlgorithm] = useState("dijkstra");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const loadNetwork = async () => {
    try {
      const response = await axios.get(`${API}/api/network`);
      setNetwork(response.data);
    } catch (error) {
      console.error("Failed to load network:", error);
    }
  };

  useEffect(() => {
    loadNetwork();
  }, []);

  const runAlgorithm = async () => {
    setLoading(true);
    setResult(null);

    try {
      let url;

      if (algorithm === "bfs") {
        url = `${API}/api/bfs?start=${start}&target=${target}`;
      } else {
        url = `${API}/api/dijkstra?start=${start}&target=${target}`;
      }

      const response = await axios.get(url);
      setResult(response.data);
    } catch (error) {
      console.error("Algorithm error:", error);

      setResult({
        found: false,
        error: "Unable to run algorithm",
      });
    }

    setLoading(false);
  };

  const failRouter = async (router) => {
    try {
      await axios.post(`${API}/api/failure/router`, {
        router,
      });

      await loadNetwork();
      setResult(null);
    } catch (error) {
      console.error("Failed to fail router:", error);
    }
  };

  const restoreRouter = async (router) => {
    try {
      await axios.post(`${API}/api/restore/router`, {
        router,
      });

      await loadNetwork();
      setResult(null);
    } catch (error) {
      console.error("Failed to restore router:", error);
    }
  };

  const resetNetwork = async () => {
    try {
      await axios.post(`${API}/api/reset`);

      await loadNetwork();
      setResult(null);
    } catch (error) {
      console.error("Failed to reset network:", error);
    }
  };

  if (!network) {
    return (
      <div className="loading">
        Loading NetworkGuard...
      </div>
    );
  }

  const routers = Object.entries(network.routers);

  const activeRouters = routers.filter(
    ([, data]) => !data.failed
  ).length;

  const failedRouters = routers.filter(
    ([, data]) => data.failed
  ).length;

  return (
    <div className="app">

      {/* HEADER */}
      <header className="header">
        <div className="header-brand">
          <span className="header-mark">
            <Network size={24} aria-hidden="true" />
          </span>
          <div className="header-copy">
            <span className="header-kicker">Network operations</span>
            <h1>NetworkGuard</h1>
            <p>Failure recovery simulator</p>
          </div>
        </div>

        <div className="header-actions">
          <span className="header-status">
            <span className="header-status-dot" />
            Live topology
          </span>
          <button
            className="reset-btn"
            onClick={resetNetwork}
          >
            <RotateCcw size={17} aria-hidden="true" />
            Reset network
          </button>
        </div>
      </header>


      <main>

        {/* LIVE NETWORK GRAPH */}
        <section className="panel graph-panel">

          <h2>
            <Network size={22} />
            Live Network Topology
          </h2>

          <NetworkGraph network={network} path={result?.path || []} />

        </section>


        {/* NETWORK STATISTICS */}
        <section className="stats">

          <div className="stat-card">

            <Server />

            <div>
              <span>Total Routers</span>

              <strong>
                {routers.length}
              </strong>
            </div>

          </div>


          <div className="stat-card">

            <Activity />

            <div>
              <span>Active Routers</span>

              <strong>
                {activeRouters}
              </strong>
            </div>

          </div>


          <div className="stat-card danger">

            <AlertTriangle />

            <div>
              <span>Failed Routers</span>

              <strong>
                {failedRouters}
              </strong>
            </div>

          </div>


          <div className="stat-card">

            <Network />

            <div>
              <span>Components</span>

              <strong>
                {network.component_count}
              </strong>
            </div>

          </div>

        </section>


        {/* DASHBOARD */}
        <section className="dashboard">


          {/* ROUTER MANAGEMENT */}
          <div className="panel">

            <h2>
              Network Routers
            </h2>

            <div className="routers">

              {routers.map(([router, data]) => (

                <div
                  key={router}
                  className={`router ${
                    data.failed
                      ? "failed"
                      : "active"
                  }`}
                >

                  <div className="router-icon">
                    <Server size={24} />
                  </div>


                  <strong>
                    {router}
                  </strong>


                  <span>
                    {data.failed
                      ? "FAILED"
                      : "ACTIVE"}
                  </span>


                  {data.failed ? (

                    <button
                      onClick={() =>
                        restoreRouter(router)
                      }
                    >
                      Restore
                    </button>

                  ) : (

                    <button
                      onClick={() =>
                        failRouter(router)
                      }
                    >
                      Fail
                    </button>

                  )}

                </div>

              ))}

            </div>

          </div>


          {/* ROUTE ANALYSIS */}
          <div className="panel">

            <h2>

              <Route size={22} />

              Route Analysis

            </h2>


            <div className="controls">


              {/* START ROUTER */}
              <label>

                Start Router

                <select
                  value={start}
                  onChange={(e) =>
                    setStart(e.target.value)
                  }
                >

                  {routers.map(([router]) => (

                    <option
                      key={router}
                      value={router}
                    >
                      {router}
                    </option>

                  ))}

                </select>

              </label>


              {/* TARGET ROUTER */}
              <label>

                Target Router

                <select
                  value={target}
                  onChange={(e) =>
                    setTarget(e.target.value)
                  }
                >

                  {routers.map(([router]) => (

                    <option
                      key={router}
                      value={router}
                    >
                      {router}
                    </option>

                  ))}

                </select>

              </label>


              {/* ALGORITHM */}
              <label>

                Algorithm

                <select
                  value={algorithm}
                  onChange={(e) =>
                    setAlgorithm(e.target.value)
                  }
                >

                  <option value="dijkstra">
                    Dijkstra
                  </option>

                  <option value="bfs">
                    BFS
                  </option>

                </select>

              </label>


              {/* RUN BUTTON */}
              <button
                className="run-btn"
                onClick={runAlgorithm}
              >
                Run Algorithm
              </button>

            </div>


            {/* LOADING */}
            {loading && (

              <div className="result">

                Running algorithm...

              </div>

            )}


            {/* RESULT */}
            {result && !loading && (

              <div className="result">

                {result.found ? (

                  <>

                    <h3>
                      Route Found
                    </h3>


                    <div className="path">

                      {result.path.map(
                        (router, index) => (

                          <span key={router}>

                            {router}

                            {index <
                              result.path.length - 1 && (
                              <b> → </b>
                            )}

                          </span>

                        )
                      )}

                    </div>


                    {/* BFS RESULT */}
                    {algorithm === "bfs" ? (

                      <p>

                        Minimum hops:{" "}

                        <strong>
                          {result.hops}
                        </strong>

                      </p>

                    ) : (

                      /* DIJKSTRA RESULT */
                      <p>

                        Total cost:{" "}

                        <strong>
                          {result.cost}
                        </strong>

                      </p>

                    )}

                  </>

                ) : (

                  <>

                    <h3>
                      No route available
                    </h3>

                    {result.error && (
                      <p>
                        {result.error}
                      </p>
                    )}

                  </>

                )}

              </div>

            )}

          </div>

        </section>

      </main>

    </div>
  );
}

export default App;