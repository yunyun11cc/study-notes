"""
给定二维网格 grid，其中 '1' 表示陆地，'0' 表示水。返回岛屿数量。

岛屿由上下左右相连的陆地组成，网格外视为水。

示例 1
输入：grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
输出：3

示例 2
输入：grid = [['1', '1'], ['0', '1']]
输出：1
"""


# 1. DFS 入口安检（终止条件）：如果坐标越界，或者当前格子不是 '1'（是水 '0' 或已访问过的 '#'），直接 return
# 2. 原地标记 + 四向扩散：把当前格子改成 '#' 防止绕圈，然后依次对上下左右 4 个相邻坐标递归调用 dfs
# 3. 外层双循环扫雷：遍历网格中的每个格子，一旦遇到 '1' 就将岛屿计数 +1，并调用 dfs(r, c) 把整座岛清理干净

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        self.m=len(grid) # 行数
        self.n=len(grid[0]) # 列数
        count=0
        
        def dfs(r,c):
            if r<0 or r>self.m-1 or c<0 or c>self.n-1:
                return
                                
            if  grid[r][c]!='1': # 不是 1 就直接返回
                return
                                    
            grid[r][c]='#'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c]=='1':
                    count+=1
                    dfs(r,c) # 开始清理所有连通的 1
        
        return count
