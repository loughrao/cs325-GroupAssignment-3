# Imports the heapq allowing us to use the heap structure in prims algorithm
import sys
import heapq

inp = open("input.txt", "r");

i = 0;
j = 0;

things = [[int(n) for n in line.rstrip("\n").split(",")]for line in inp];	
X = things[0][0];
array = [[0]*X]*X;
for i in range(X):
	array[i] = things[i+1]

Tv  = [0]*X
h   = []
mst = []
mins = []
j = 0;

Tv[0] = 1

for i in range(0,X) :
  if ( Tv[i] == 0 ) :
    heapq.heappush(h, (array[0][i],i))

while (len(h) != 0) :
  current = []
  ue = heapq.heappop(h)
  if (Tv[ue[1]] == 0) :
    mst.append(ue[0])
    Tv[ue[1]] = 1
    for i in range(0,X) :
      if ( Tv[i] == 0 ) :
        heapq.heappush(h, (array[ue[1]][i],i))
      if ( array[ue[1]][i] != 0 ) :
        dif = abs(array[ue[1]][i]-ue[0])
        heapq.heappush(mins, (dif, array[ue[1]][i]))
min1 = 0
min2 = 0
while (len(mins) != 0) :
  c = heapq.heappop(mins)
  flag = 1
  print(c[0])
  for i in range(len(mst)) :
      if (c[1] == mst[i]) :
        flag = 0
  if (flag) :
    if (min1 == 0):
      min1=c[0]
      min2=c[0]
    elif (min1 != 0):
      min2=c[0]     
        
mst1 = sum(mst)
mst2 = sum(mst)+min1
mst3 = sum(mst)+min2
print(mst1)
print(mst2)
print(mst3)
