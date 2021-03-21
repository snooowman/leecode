# -*- coding:utf-8 -*-
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x**n
        res = 1
        if n<0:
            n=-n
            x=1/x
        while n>0:
            if n%2:
                res = res*x
            x *= x
            n = int(n/2)
        return res


if __name__ == '__main__':
    s=Solution()
    print(s.myPow(2.0000, 2))