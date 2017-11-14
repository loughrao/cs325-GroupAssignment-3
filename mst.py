# Imports the heapq allowing us to use the heap structure in prims algorithm
import heapq

V = 3
array = [[0]*V]*V
array[0] = [0,6,2]
array[1] = [6,0,10]
array[2] = [2,10,0]

print(array)

Tv = []
Te = []
h  = []

v  = 0

Tv.append(v)
for i in range(0,V) :
  if ( i != v ) :
    heapq.heappush(h, (array[v][i],i))

while (len(h) != 0) :
  ue = heappop(h)
  if ( 
