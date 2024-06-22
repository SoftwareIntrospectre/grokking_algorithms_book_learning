"""

In each of these graphs, what is the weight of the shortest path from start to finish?


A.
                  4
            >()------>()
         5 / | \      | \ 3
          /  |  \     |  \
    Start() 8|  2\    |6   > () Finish
          \  |    \   |  / 1
         2 \ |     \  | /
            >()----->>()
                  7

B.
                20
         ()-------------->()
          ^              /\
      10/   \           /  \ 30
       /     \         /    \
      /     1 \       / 1    v
Start()        \     /       () Finish
                \   /
                 \ v
                  ()



C.

             >()------------
            / ^ \          |
         2 /  |  \         | 2
          /   |   \ 2      v
    Start() 2 |    \     > () Finish
          \   |     \   / 2
         2 \  |      \ /
            >()----->()
                  -1

                  
Answer:

Graph A = 8 (2 -> 7 -> 1)
Graph B = 60 (10 -> 20 -> 30)
Graph C = 4 (2 -> 2)

"""