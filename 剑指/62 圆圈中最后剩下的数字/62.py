# -*- coding:utf-8 -*-
class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        #约瑟夫环
        x = 0
        for i in range(2, n+1):
            x = (x+m) % i
        return x

if __name__ == '__main__':
    s=Solution()
    print(s.lastRemaining(5, 3))