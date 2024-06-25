
# arr = [1,2,2,3,3,3]
# print(arr)

# print(set(arr))

#---------------------#

"""
Suppose you're starting a radio show. You want to reach listeners to all 50 USA states.
You have to decide what stations to play on to reach all those listeners.
It costs money to to be on each station, so you're trying to minimize the number of stations you play on.
You have a list of stations.

Each station covers a region, and there's overalap.

Howw do you figure out the smallest set of stations you can play on to cover all 50 states?
"""


"""
    Below: Implement a Greedy Approximation Algorithm to find the "closest to optimal" solution, because the optimal solution is super difficult.
"""
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # you pass an array in, and it gets converted to a set
stations = {}

stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:

    best_station = None
    states_covered = set()

    for station, states in stations.items(): 
        covered = states_needed & states # syntax: set intersection (basically an INNER JOIN)
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(f"final_stations: {final_stations}")

# final output is: final_stations: {'ktwo', 'kone', 'kthree', 'kfive'}
# This is not in-order, but is close enough with useful information.


"""Playing with Union, Intersection, and Difference logic (set theory, used to this.)"""
# fruits = set(["avocado", "tomato", "banana"])
# vegetables = set(["beets", "carrots", "tomato"])

# print(f"fruits: {fruits}")
# print(f"vegetables: {vegetables}")

# # this is a UNION
# print(f"union: {fruits | vegetables}")

# # this is an intersection (INNER JOIN)
# print(f"intersection: {fruits & vegetables}")

# # this is a difference (LEFT JOIN where vegatables IS NULL)
# print(f"difference: fruits - vegatables: {fruits - vegetables}")

# # this is a difference (LEFT JOIN where fruits IS NULL)
# print(f"difference: vegetables - fruits: {vegetables - fruits}")