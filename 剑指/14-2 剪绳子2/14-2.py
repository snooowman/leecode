# -*- coding:utf-8 -*-
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
    # 递归存中间值
        if n == 2:
            return 1
        self.memo = [0] * (n+1)
        self.memo[2] = 1
        r = self.F(self.memo, n)
        p = 1000000007
        return int(r % p)

    def F(self, memo, n):
        if memo[n] != 0:
            return memo[n]
        ret = 0
        for i in range(2,n):
            ret = max(ret, max(i*(n-i),i*self.F(memo, n-i)))
        memo[n] = ret
        return ret
        # p = int(1e9 + 7)
        # return int(self.dp[n] * n % p)

        # # 递归
        # if n <= 2:
        #     return n - 1
        # ret = 0
        # for i in range(2, n):
        #     ret = max(ret, max(i * (n - i), i * self.cuttingRope(n - i)))
        # return ret

        # # 动态规划
        # self.dp = [0] * (n + 1)
        # self.dp[2] = 1
        # for i in range(3, n+1):
        #     for j in range(2,i):
        #         self.dp[i] = max(self.dp[i], max(j*self.dp[i-j], j*(i-j)))
        # return self.dp[n]






if __name__ == '__main__':
    s=Solution()
    print(s.cuttingRope(10))