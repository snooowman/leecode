# -*- coding:utf-8 -*-
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划
        a = 1
        b = 1
        for _ in range(n):
            a, b = a+b, a
        return b%1000000007



if __name__ == '__main__':
    s=Solution()
    print(s.numWays(10))