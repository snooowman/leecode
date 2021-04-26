# -*- coding:utf-8 -*-
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        n = a^b
        c = (a&b)<<1
        res = n + c
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.add(1,1))