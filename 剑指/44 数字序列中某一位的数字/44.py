# -*- coding:utf-8 -*-
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b, c = 1, 1, 9
        # 1求出digit-a n所在位数
        while n > c:
            n -= c
            a += 1
            b *= 10
            c = 9 * a * b
        # 2求出所在的数
        num = b + (n - 1) / a
        # 3求出所在的值
        s = str(num)
        res = int(s[(n - 1) % a])
        return res



if __name__ == '__main__':
    s=Solution()
    print(s.findNthDigit(10))