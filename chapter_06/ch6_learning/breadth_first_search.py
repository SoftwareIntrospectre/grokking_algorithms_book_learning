# imports Doubly Ended Queue (queue data structure)
from collections import deque 

# import local file: graph.py
import graph


# works if the last letter of a person's name ends with "m" (arbitrary condition in this case)
def person_is_seller(name):
    print("person_is_seller() check: " , name)
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph.graph(name)
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            
            else:
                search_queue += graph.graph[person]
                searched.add(person)

    return False


def find_mango_seller_from_graph(search_queue):

    # while the queue is not empty:
    while search_queue: 

        # grabs the first person off the queue
        person = search_queue.popleft()
        print("person --> search_deque.popleft(): " , person)

        # checks whether the person is a mango seller
        if person_is_seller(person):
            print(person , " is a mango seller!")
            return True
        
        else:
            print("search_queue: " , search_queue)
            search_queue += graph.graph[person]
            print("search_queue updated: " , search_queue)

    return False

search_queue = deque(graph.graph["you"])
print("graph['you']: ", graph.graph["you"])
print("search_queue: ", search_queue)

find_mango_seller_from_graph(search_queue)

search('Alice')