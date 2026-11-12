"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
    
"""




class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer=[] # 答案数组
        prefix=1 #前缀积，初始化为1
        n=len(nums)

        # 先在ans中算出所有元素的前缀积
        for i in range(n):
            answer.append(prefix)
            prefix*=nums[i]
        
        suffix=1 # 后缀积，从n-1开始往前算
        for i in range(n - 1, -1, -1):
            answer[i]*=suffix
            suffix*=nums[i]

        return answer