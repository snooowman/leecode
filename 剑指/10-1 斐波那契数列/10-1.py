# -*- coding:utf-8 -*-
l = []
l.append(0)
l.append(1)

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #递归超时
        # if n == 0 or n == 1:
        #     return n
        # else:
        #     return self.fib(n-1) + self.fib(n-2)
        #记忆递归
        if n == 0 or n == 1:
            return n
        else:
            if len(l)>n:
                return l[n]
            l.append(self.fib(n-1) + self.fib(n-2))
            return l[n]
        #动态规划
        # a = 1
        # b = 0
        # for _ in range(n):
        #     a, b = a+b, a
        # return b%1000000007


if __name__ == '__main__':
    s=Solution()
    print(s.fib(10))