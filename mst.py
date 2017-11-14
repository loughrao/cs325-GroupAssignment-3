# Imports the heapq allowing us to use the heap structure in prims algorithm
import heapq

inp = open("input.txt", "r");

i = 0;
j = 0;

things = [[int(n) for n in line.rstrip("\n").split(",")]for line in inp];	
X = things[0][0];
array = [[0]*X]*X;
for i in range(X):
	array[i] = things[i+1]

Tv  = []
Te  = []
h   = []
ans = 0

v  = 0

Tv.append(v)
for i in range(0,X) :
  if ( i != v ) :
    heapq.heappush(h, (array[v][i],i))

while (len(h) != 0) :
  ue = heapq.heappop(h)
  ans = ans + ue[0] 

print(ans)
