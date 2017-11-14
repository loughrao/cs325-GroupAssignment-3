inp = open("input.txt", "r");
i = 0;
j = 0;
X = 0;
things = [[int(n) for n in line.rstrip("\n").split(",")]for line in inp];	
print(things)
X = things[0][0];
array = [[0]*X]*X;
for i in range(X):
	array[i] = things[i+1]
print(array)
