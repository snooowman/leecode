# -*- coding:utf-8 -*-
import functools
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def sort_func(a, b):
            x, y = a + b, b + a
            if x > y:
                return 1
            elif x < y:
                return -1
            else:
                return 0
        numss = [str(num) for num in nums]
        numss.sort(key=functools.cmp_to_key(sort_func))
        print(numss)
        return ''.join(numss)

if __name__ == '__main__':
    s=Solution()
    print(s.minNumber([3,30,34,5,9]))