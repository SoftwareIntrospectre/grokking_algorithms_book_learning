import math

graph = {}
graph["you"] = ["alice", "bob", "claire"]


# graph with weighted edges
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# print(graph)
print(list(graph["start"].keys()))
print(list(graph["start"].values()))


graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # this finish node doesn't have any out-neighbors

print(graph)


infinity = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

print(costs)

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = set()

"""
    Algorithm:

    --> [While we have nodes to process:]
    |           |
    |           v
    |    [Grab the node that is closest to the start]
    |           |
    |           v
    |   [update costs for its neighbors]
    |           |
    |           v
    |   [if any of the neighbors' costs were updated, update the parent too]
    |           |
    |           v
    |---[Mark this node processed]

"""

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None

    # goes through each node
    for node in costs:
        cost = costs[node]


        # if it's the lowest cost so far and hasn't been processed yet
        if cost < lowest_cost and node not in processed:

            # sets it as the new lowest-code node
            lowest_cost = cost
            lowest_cost_node = node
    
    return lowest_cost_node

# finds the lowest-cost node you haven't processed yet
node = find_lowest_cost_node(costs)

# if you've processed all the nodes, this while loop is done
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    # goes through all the out-neighbors of this node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]

        #  if it's cheaper to get this out-neighbor by going through this node...
        if costs[n] > new_cost:

            # updates the cost for the neighbor
            costs[n] = new_cost

            # this node becomes the new parenet for this out-neighbor
            parents[n] = node

    # marks the node as processed
    processed.add(node)

    # finds the next node to process and loops
    node = find_lowest_cost_node(costs) 

