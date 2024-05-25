graph = {}

graph["you"] = ["alice", "bob", "clair"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


graph2 = {}

graph2["you"] = ["alice", "bob", "clair"]
graph2["bob"] = ["anuj","peggy"]
graph2["alice"] = ["peggy"]
graph2["anuj"] = []
graph2["claire"] = ["thom", "jonny"]
graph2["peggy"] = []
graph2["thom"] = []
graph2["jonny"] = []


# proof that the order of inserts don't matter. Consistent results. (directed graph in this case)
print(graph["claire"])
print(graph["anuj"])

print(graph2["claire"])
print(graph2["anuj"])
