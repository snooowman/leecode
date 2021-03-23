# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # l1=[]
        # l2=[]
        # for i in nums:
        #     if i%2:
        #         l1.append(i)
        #     else:
        #         l2.append(i)
        # return l1+l2

        # #首尾双指针
        # left=0
        # right=len(nums)-1
        # temp = 0
        # while left < right:
        #     if nums[left]%2 and nums[right]%2 == 0:
        #         left+=1
        #         right -= 1
        #     elif nums[left]%2 == 1 and nums[right]%2 != 0:
        #         left += 1
        #     elif nums[left] % 2 != 1 and nums[right] % 2 == 0:
        #         right -=1
        #     elif nums[left] % 2 != 1 and nums[right] % 2 != 0:
        #         temp = nums[right]
        #         nums[right] = nums[left]
        #         nums[left] = temp
        # return nums

        #快慢指针
        fast = 0
        low = 0
        for i in range(len(nums)):
            if nums[fast] %2 :
                temp = nums[fast]
                nums[fast] = nums[low]
                nums[low] = temp
                low +=1
            fast+=1
        return nums



if __name__ == '__main__':
    s=Solution()
    print(s.exchange([1,2,3,4]))