# -*- coding:utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序
        # nums.sort()
        # return nums[int(len(nums)/2)]

        #hash map
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
                if dic[i] > int(len(nums)/2):
                    return i
            else:
                dic[i] = 1

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))