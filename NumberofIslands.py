class Solution():

    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        # print(row,col)
        ans = 0
        def dfs(r,c):
            d = [0, 1, 0, -1, 0]
            if r < 0 or r > row -1 or c < 0 or c > col - 1 or grid[r][c] == '0':
                return 0
            grid[r][c] = '0'
            for i in range(0,4):
                dfs(r+d[i],c+d[i+1])
            return 1

        if len(grid) == 0:
            return 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] =="1":
                    ans += dfs(r,c)
        return  ans













x = Solution()
print(x.numIslands([["1"],["1"]]))