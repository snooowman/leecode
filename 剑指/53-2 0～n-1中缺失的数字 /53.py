# -*- coding:utf-8 -*-
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0,len(nums)-1
        while i<=j:
            m = int((i+j)/2)
            if nums[m]==m:
                i = m+1;
            else:
                j = m-1;
        return i


if __name__ == '__main__':
    s=Solution()
    print(s.missingNumber([0,1]))