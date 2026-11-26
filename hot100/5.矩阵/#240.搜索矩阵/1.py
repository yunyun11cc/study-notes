"""
在 m × n 的矩阵 matrix 中查找 target。每行从左到右、每列从上到下均按升序排列。
找到目标时返回 true，搜索结束仍未找到时返回 false。

示例 1
输入：matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]], target = 5
输出：true

示例 2
输入：matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]], target = 10
输出：false
"""


# 1. 从矩阵右上角开始，当前位置是剩余区域本行的最大值和本列的最小值。
# 2. 目标比当前位置小就左移一列，比当前位置大就下移一行。
# 3. 找到目标时返回 true，行或列越出边界时返回 false。


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        top,right=0,n-1

        while top<=m-1 and right>=0:
            if target==matrix[top][right]:
                return True
            elif target < matrix[top][right]:
                # 当前列最小的候选值已经大于目标。
                right-=1
            else:
                # 当前行最大的候选值仍小于目标。
                top += 1


        return False
