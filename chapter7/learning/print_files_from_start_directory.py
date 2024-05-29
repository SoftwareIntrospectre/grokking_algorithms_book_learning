from os import listdir
from os.path import isfile, join, dirname, abspath
from collections import deque

def printnames(start_dir):

    # Use a (doubly ended) queue to keep track of directory to search
    search_queue = deque()
    search_queue.append(start_dir)

    # while the queue is not empty, pop off a directory to look through
    while search_queue:
        dir = search_queue.popleft()

        ## loop through every file and directory in this directory
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)

            # if item is a file: print out the name
            if isfile(fullpath):
                print(file)

            else:

                # if it is a directory, add it to the queue of directories to search
                search_queue.append(fullpath)


# grabbing two directories up from the current directory
current_dir = dirname(abspath(__file__))
two_levels_up_start_dir = abspath(join(current_dir, '..', '..'))


# Trees don't have cycles, and only one parent. No need to keep track because infinite loop cannot happen.
printnames(two_levels_up_start_dir)