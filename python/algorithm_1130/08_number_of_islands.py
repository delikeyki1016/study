# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1': # 상하좌우는 그리드 범위 내에 있어야 함.
                return
            grid[i][j] = '0' # 1 자리를 0으로 바꿈 
            dfs(i-1, j) # 상
            dfs(i+1, j) # 하
            dfs(i, j-1) # 좌
            dfs(i, j+1) # 우
            
        count = 0
        # grid[0][0] -> grid[3][4] 이중for문 반복 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # grid[i][j] == 1인 경우 dfs 호출
                if grid[i][j] == '1':
                    dfs(i,j) # 상하좌우 체크
                    count += 1
                    print(count, grid)
        return count
    
sol = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
result = sol.numIslands(grid)
print(result)