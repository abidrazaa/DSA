# s = 'abcd'
# t = 'bcde'
# s = 'abyz'
# t = 'bcza'

# character_map = {chr(i): i for i in range(ord('a'), ord('z')+1)}

# def checkStrings(s,t):
#     for i in range(len(s)):
#         if character_map[s[i]] == character_map[t[i]]-1:
#             continue
#         elif s[i]=='z' and character_map[t[i]]==character_map['a']:
#             continue
#         else:
#             return False

#     return True

# print(checkStrings(s,t))


def countMatches(grid1, grid2):
    def dfs(i, j, grid, visited, current_region):
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[0])
            or grid[i][j] == "0"
            or visited[i][j]
        ):
            return

        visited[i][j] = True
        current_region.append((i, j))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(i + dx, j + dy, grid, visited, current_region)

    def findRegions(grid):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        regions = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    current_region = []
                    dfs(i, j, grid, visited, current_region)
                    regions.append(current_region)

        return regions

    regions1 = findRegions(grid1)
    regions2 = findRegions(grid2)

    matched_regions = 0

    for region1 in regions1:
        for region2 in regions2:
            if set(region1) == set(region2):
                matched_regions += 1

    return matched_regions

# Example usage:
grid1 = ["001", "011", "100"]
grid2 = ["001", "011", "101"]
result = countMatches(grid1, grid2)
print(result)