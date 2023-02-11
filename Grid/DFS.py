
def traverse(grid):
    
    visited = [[False for i in grid[0]] for y in grid]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if visited[row][col]:
                continue
            dfs(row,col,grid,visited)

def dfs(row,col,grid,visited):
    stack = [(row,col)]

    while len(stack):
        x,y = stack.pop()
        
        # in case of BFS
        # x,y = stack.pop(0)

        if visited[x][y]:
            continue

        print(grid[x][y], end=",")

        visited[x][y] = True
        neighbors = getNeighbors(x,y,grid)
        stack.extend(neighbors)
    

def getNeighbors(row,col,grid):
    toVisitNext = []
    if col>0:
        toVisitNext.append((row,col-1))
    if col<len(grid[0])-1:
        toVisitNext.append((row,col+1))
    if row>0:
        toVisitNext.append((row-1,col))
    if row<len(grid)-1:
        toVisitNext.append((row+1,col))

    return toVisitNext

grid = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

traverse(grid)