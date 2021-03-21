# -*- coding:utf-8 -*-
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # res = []
        # i = 1
        # print(10**n)
        # while i < (10**n):
        #     res.append(i)
        #     i+=1
        # return res

        res = []
        for i in range(1,10**n):
            res.append(i)
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.printNumbers(1))