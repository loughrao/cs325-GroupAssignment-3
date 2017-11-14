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

T  = [0]*X
h   = []
c   = []
ans = 0

T[0] = 1

for i in range(0,X) :
  if ( i != 0 ) :
    heapq.heappush(h, (array[0][i],i))

while (len(h) != 0) :
  ue = heapq.heappop(h)
  if (T[ue[1]] == 0) :
    ans = (ans + ue[0])
    T[ue[1]] = 1
    for i in range(0,X) :
      if ( i != ue[1] ) :
        heapq.heappush(h, (array[ue[1]][i],i))

print(ans)
