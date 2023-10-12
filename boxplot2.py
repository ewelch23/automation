# boxplot2.py

import math
import matplotlib.pyplot as plt

with open("runtimes.txt") as f:
    bfs_runtimes = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))
    dfs_runtimes = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))
    astar_runtimes = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))

bfs_runtimes = list(filter(lambda x: not math.isnan(x), bfs_runtimes))
dfs_runtimes = list(filter(lambda x: not math.isnan(x), dfs_runtimes))
astar_runtimes = list(filter(lambda x: not math.isnan(x), astar_runtimes))

with open("nodes.txt") as f:
    bfs_nodes = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))
    dfs_nodes = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))
    astar_nodes = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))

bfs_nodes = list(filter(lambda x: not math.isnan(x), bfs_nodes))
dfs_nodes = list(filter(lambda x: not math.isnan(x), dfs_nodes))
astar_nodes = list(filter(lambda x: not math.isnan(x), astar_nodes))

with open("cost.txt") as f:
    bfs_cost = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))
    dfs_cost = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))
    astar_cost = list(map(float, f.readline().strip().replace('[', '').replace(']', '').split(', ')))

bfs_cost = list(filter(lambda x: not math.isnan(x), bfs_cost))
dfs_cost = list(filter(lambda x: not math.isnan(x), dfs_cost))
astar_cost = list(filter(lambda x: not math.isnan(x), astar_cost))


fig, axs = plt.subplots(3, 2)
fig.set_size_inches(6,4, forward=True)
fig.set_dpi(100)
fig.suptitle('Boxplots for BFS, DFS, & A*')
axs[0,0].boxplot([bfs_runtimes,dfs_runtimes,astar_runtimes], vert=True, showmeans=True, labels=["BFS","DFS","A*"])
axs[0,0].set_ylabel("Runtime (seconds)")
axs[0,1].boxplot(astar_runtimes, vert=True, showmeans=True, labels=["A*"])

axs[1,0].boxplot([bfs_nodes,dfs_nodes,astar_nodes], vert=True, showmeans=True, labels=["BFS","DFS","A*"])
axs[1,0].set_ylabel("Nodes")
axs[1,1].boxplot(astar_nodes, vert=True, showmeans=True, labels=["A*"])

axs[2,0].boxplot([bfs_cost,astar_cost], vert=True, showmeans=True, labels=["BFS","A*"])
axs[2,0].set_ylabel("Cost")
axs[2,1].boxplot(dfs_cost, vert=True, showmeans=True, labels=["DFS"])
plt.show()