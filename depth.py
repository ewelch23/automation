import time
from queue import LifoQueue
import gridworld as gw
import numpy as np

def action_state(x,y,action):
    if action == "left":
        new_x = x-1
        new_y = y
    elif action == "right":
        new_x = x+1
        new_y = y
    elif action == "down":
        new_y = y+1
        new_x = x
    elif action == "up":
        new_y = y-1
        new_x = x
    else:
        new_y = y
        new_x = x
    return new_x, new_y

def state_action(state1,state2):
    x1 = state1['x']
    x2 = state2['x']
    y1 = state1['y']
    y2 = state2['y']
    if x1>x2:
        action = "left"
    elif x1<x2:
        action = "right"
    elif x1==x2:
        if y1<y2:
            action = "down"
        elif y1>y2:
            action = "up"
        elif y1==y2:
            raise ValueError("Impossible action!")
    return action

def search_xy(states, x, y):
    for pot_state in states:
        if pot_state['x'] == x and pot_state['y'] == y:
            state = pot_state
    return state

def dfs(states, start_loc):
    queue = LifoQueue()  # paths go inside a queue
    visited = set()  # creates empty set
    start_state = search_xy(states,start_loc['x'],start_loc['y'])
    queue.put([start_state])  # lists of states = node -> go into queue
    while not queue.empty():
        path = queue.get()  # obtains shallowest path
        current_state = path[-1]  # possible actions come from this state
        for child_action in current_state['possible_actions']:
            curr_x = current_state['x']
            curr_y = current_state['y']
            child_x, child_y = action_state(curr_x,curr_y,child_action)
            child_state = search_xy(states, child_x, child_y)
            if (child_x,child_y) not in visited:  # to not waste computation time
                child_path = path + [child_state]
                queue.put(child_path)  # put the child in queue if need
                if child_state['goal'] is True:
                    return child_path, visited
                visited.add((child_x,child_y))

def dfs_actions(states, start_states):
    solution_path,solution_nodes = dfs(states, start_states)
    solution_actions = []
    for i in range(0,len(solution_path)-1):
        solution_actions.append(state_action(solution_path[i], solution_path[i+1]))
    return solution_actions, len(solution_nodes), len(solution_actions)

## to run the 4 standard grids
# for grid_name, grid in [('grid_1',gw.grid1), ('grid_2',gw.grid2),('random_grid_10x10',gw.random_grid10),('random_grid_100x100',gw.random_grid100)]:
#     print("Performing DFS for " + grid_name)
#     grid_dict = gw.create_grid_dict_from_array(grid)
#     gw.plot_grid(grid_dict,grid)
#     start = time.time()
#     move_sequence = dfs_actions(grid_dict["node_list"], grid_dict["start_location"])
#     end = time.time()
#     print("Runtime: " + str(end-start) + " seconds")
#     gw.plot_path(grid_dict,grid,move_sequence,f_name=str('DFS_')+grid_name+str('.png'))

i=0
runtime_dfs = []  # store the runtimes so i can make a plot
nodes_dfs = []
cost_dfs = []
total_start = time.time()
while i<100:
    try:
        random_grid100 = np.zeros((100,100))
        walls = np.random.choice(random_grid100.size, 2000, replace=False)
        goals = np.random.choice(random_grid100.size, 1, replace=False)
        start = np.random.choice(random_grid100.size, 1, replace=False)
        random_grid100.ravel()[walls] = np.nan
        random_grid100.ravel()[goals] = 1
        random_grid100.ravel()[start] = 5
        grid_dict = gw.create_grid_dict_from_array(random_grid100)
        start = time.time()
        move_sequence, num_nodes, cost = dfs_actions(grid_dict["node_list"], grid_dict["start_location"])
        end = time.time()
        runtime_dfs.append(end-start)
        nodes_dfs.append(num_nodes)
        cost_dfs.append(cost)
        print("grid # " + str(i) + " ran in " + str(end-start))
        i += 1
    except TypeError:
        print("No solution found...")  # if no solution is found, the code makes another grid to cover it
        runtime_dfs.append(np.nan)
total_end = time.time()
print("Total runtime for " +str(i) +" grids " + str((total_end-total_start)/60) + ' minutes.')

with open('runtimes.txt', 'a') as f:
    f.writelines(str(runtime_dfs)+'\n')

with open('nodes.txt', 'a') as f:
    f.writelines(str(nodes_dfs)+'\n')

with open('cost.txt', 'a') as f:
    f.writelines(str(cost_dfs)+'\n')
