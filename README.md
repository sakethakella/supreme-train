
---

# Interference-Constrained Frequency Assignment

## Project Overview

**Spectrum.AI** addresses the critical challenge of **Spectral Efficiency** in modern wireless networks (5G/IoT). As network density increases, assigning frequencies to base stations becomes a complex optimization problem.

We model this as an **Interference-Constrained Frequency Assignment Problem (IC-FAP)**, utilizing Classical AI techniques to minimize signal degradation and maximize spectrum reuse.

### The Problem: IC-FAP

In dense deployments, overlapping frequency assignments lead to:

1. **Co-Channel Interference (CCI):** Nodes within an interference radius using the same frequency.
2. **Adjacent-Channel Interference (ACI):** Signal leakage when proximate nodes use neighboring frequency bands.


## 🧠 AI Strategy: Constraint Satisfaction Problem (CSP)

To solve the IC-FAP, we treat the network as a graph where towers are nodes and interference constraints are edges.

### 1. State Space Representation

* **Variables ($X$):** A set of Base Stations $\{B_1, B_2, \dots, B_n\}$.
* **Domains ($D$):** Available discrete frequency channels $\{f_1, f_2, \dots, f_m\}$.
* **Constraints ($C$):** * **Hard Constraint (CCI):** $f_i \neq f_j$ for nodes within interference range.
* **Soft/Proximity Constraint (ACI):** $|f_i - f_j| > \delta$ for nodes in extreme proximity.



### 2. Algorithms & Heuristics

We implement **Backtracking Search** enhanced by **Maintaining Arc Consistency (MAC)** and the following heuristics:

* **MRV (Minimum Remaining Values):** Prioritizes towers with the fewest legal frequency options.
* **Degree Heuristic:** Tie-breaker for nodes with the most constraints on unassigned neighbors.
* **LCV (Least Constraining Value):** Chooses frequencies that leave the most flexibility for neighbors.
* **AC-3 Algorithm:** Pre-processing and real-time inference to prune the search space.

---

## 📊 Implementation & Visualization

Our implementation includes a dynamic Python-based dashboard to visualize the AI's "thought process" in real-time.

* **Dynamic Graph Layout:** Using `NetworkX` to represent towers and interference edges.
* **Search Animation:** Visualizing the backtracking process (nodes flashing on failure) and domain shrinking.
* **Metrics:** Real-time tracking of **Spectrum Reuse Density** vs. **Total Channels Used**.

### Tech Stack

* **Language:** Python 3.x
* **Libraries:** `NetworkX`, `Plotly`, `Dash` (or `Matplotlib`), `NumPy`

---

## 🚀 Getting Started

*(Note: These are placeholders for your future implementation)*

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/Spectrum-AI.git

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the simulation:**
```bash
python main.py

```



---

**Course:** AI Foundations and Applications (AI61005) | **IIT Kharagpur**
