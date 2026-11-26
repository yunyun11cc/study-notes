"""
给定一个 m × n 的矩阵 matrix，从左上角出发，按顺时针方向一圈一圈向内遍历。
返回按访问顺序排成的元素列表。

示例 1
输入：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
输出：[1, 2, 3, 6, 9, 8, 7, 4, 5]

示例 2
输入：matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
输出：[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""


# 1. 用 top、bottom、left、right 记录当前未遍历区域的四条边。
# 2. 每轮按上、右、下、左依次访问，每处理一条边就收缩对应边界。
# 3. 访问每条边前检查对应边界，避免只剩一行或一列时重复访问。


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m=len(matrix)
        n=len(matrix[0])
        result=[]

        top, bottom, left, right = 0, m-1, 0, n-1

        # 每访问完一条边，就将其排除在剩余矩阵之外。
        while top <= bottom and left <= right:
            if top <= bottom:
                for j in range(left,right+1):
                    result.append(matrix[top][j])
                top+=1

            if left <= right:
                for i in range(top,bottom+1):
                    result.append(matrix[i][right])
                right-=1

            # 前面可能已访问了最后一行，先确认底边仍存在。
            if top <= bottom:
                for j in range(right,left-1,-1):
                    result.append(matrix[bottom][j])
                bottom-=1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1


        return result
