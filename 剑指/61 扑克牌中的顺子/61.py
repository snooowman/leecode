# -*- coding:utf-8 -*-
class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ma = 0
        mi = 14
        repeat = []
        for i in nums:
            if i == 0:
                continue
            if i > ma:
                ma = i
            if i < mi:
                mi = i
            if i not in repeat:
                repeat.append(i)
            else:
                return False
        print(ma)
        print(mi)
        if ma - mi < 5:
            return True
        else:
            return False



if __name__ == '__main__':
    s=Solution()
    print(s.isStraight([0,3,4,13,9]))