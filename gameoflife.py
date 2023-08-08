x='X' # dead
o='O' # alive

grid=[]

m = 11 # num rows
n = 10 # num cols

for i in range(m):
    a = []
    for j in range(n):
        a.append(x)
    grid.append(a)

grid[5][5] = o
grid[4][5] = o
grid[4][6] = o
print(grid)


# Make the rules
iterations = 1
for k in range(iterations):

    for i, row in enumerate(grid):

        for j, cell in enumerate(row):
            # Any live cell with two or three live neighbours survives.

            livingNeighbors = 0
            for horizontal in range(3):
                horizontal += -1
                

                if horizontal + j < 0 or horizontal + j > n-1:
                    continue

                for vertical in range(3):
                    # Make them be in {-1, 0, 1}
                    vertical += -1


                    if vertical + i < 0 or vertical + i > m-1:
                        continue
                    
                    if vertical + i == 0 and horizontal + j == 0:
                        continue

                    if grid[i + vertical][j + horizontal] == o:
                        livingNeighbors += 1

            print("row: ", i, "col: ", j, "neighbors: ", livingNeighbors)

                    


