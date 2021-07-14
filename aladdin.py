
import queue


# function to calculate no of nodes
# between two nodes
def totalNodes(adjac, n, x, y):
    # x is the source node and
    # y is destination node

    # visited array take account of
    # the nodes visited through the bfs
    visited = [0] * (n + 1)

    # parent array to store each nodes
    # parent value
    p = [None] * n

    q = queue.Queue()
    q.put(x)

    # take our first node(x) as first
    # element of queue and marked it as
    # visited through visited[] array
    visited[x] = True

    m = None

    # normal bfs method starts
    while (not q.empty()):
        m = q.get()
        for i in range(len(adjac[m])):
            h = adjac[m][i]
            if (not visited[h]):
                visited[h] = True

                # when new node is encountered
                # we assign it's parent value
                # in parent array p
                p[h] = m
                q.put(h)

    # count variable stores the result
    count = 0

    # loop start with parent of y
    # till we encountered x
    i = p[y]
    while (i != x):
        # count increases for counting
        # the nodes
        count += 1

        i = p[i]

    return count

n, h, x = map(int, input().split())  # n is number of cities,h is number of hotsopts,x is distance virus can travel
hotspot = list(map(int, input().split()))  # city numbers marked as hotspots
adjac = [[] for i in range(n+1)]
a=0
for _ in range(n-1):
    u, v = map(int, input().split())

    # creating graph, keeping length of
    # adjacency list as (1 + no of nodes)
    # as index ranges from (0 to n-1)
    adjac[u].append(v)
    adjac[v].append(u)



if h>2 :
    start= hotspot[0]
    for i in range(1,h):
        end=hotspot[i]
        b = totalNodes(adjac, n + 1, hotspot[start], hotspot[end])
        if b<=x:
            a=a+b
    print(a+h)
else:
    b = totalNodes(adjac, n + 1, hotspot[0], hotspot[1])
    if b <=x:
        print(b+h)





