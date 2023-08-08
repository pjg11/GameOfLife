x='X' # dead
o='O' # alive

grid=[]

for i in range(10):
    a = []
    for j in range(10):
        a.append(x)
    grid.append(a)

grid[5][5] = o
grid[4][5] = o
grid[4][6] = o
print(grid)