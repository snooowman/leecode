# -*- coding:utf-8 -*-
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret =0
        while n:
            ret += n&1
            n>>=1
        return ret


if __name__ == '__main__':
    s=Solution()
    print(s.hammingWeight(0b00001101))