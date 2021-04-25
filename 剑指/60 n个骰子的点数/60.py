# -*- coding:utf-8 -*-
class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp = [1.0/6.0] * 6
        for i in range(2, n+1):
            tmp = [0] * (5*i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        return dp


if __name__ == '__main__':
    s=Solution()
    print(s.dicesProbability(1))