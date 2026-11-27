"""
有 numCourses 门课，编号从 0 到 numCourses - 1。
prerequisites 中的每对 [a, b] 表示必须先完成课程 b，才能学习课程 a。
如果存在一种能修完所有课程的顺序，返回 True，否则返回 False。

示例 1
输入：numCourses = 3, prerequisites = [[1, 0], [2, 1]]
输出：True
解释：可以依次学习 0、1、2。

示例 2
输入：numCourses = 2, prerequisites = [[1, 0], [0, 1]]
输出：False
解释：两门课程都要求先完成另一门。
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pass
