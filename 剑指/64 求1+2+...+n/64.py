# -*- coding:utf-8 -*-
class Solution(object):
    res = 0
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        n>0 and self.sumNums(n-1)
        self.res += n
        return self.res


if __name__ == '__main__':
    s=Solution()
    print(s.sumNums(3))