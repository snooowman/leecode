# -*- coding:utf-8 -*-
import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力1
        # res = -sys.maxsize -1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         temp = -sys.maxsize -1
        #         if j > i:
        #             temp = 0
        #             for l in range(i, j+1):
        #                 temp += nums[l]
        #         elif i == j:
        #             temp = nums[i]
        #         if temp > res:
        #             res = temp
        # return res

        # 暴力2
        # res = -sys.maxsize - 1
        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(i,len(nums)):
        #         temp += nums[j]
        #         if temp > res:
        #             res = temp
        # return res

        # 动态规划
        for i in range(1,len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)



if __name__ == '__main__':
    s=Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))