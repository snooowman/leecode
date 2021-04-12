# -*- coding:utf-8 -*-
class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 迭代
        s = str(num)
        a = b = 1
        c = 0
        for i in range(2, len(s)+1):
            print(s[i-2:i])
            c = a + b if '10'<=s[i-2:i]<='25' else a
            b = a
            a = c
        return c


if __name__ == '__main__':
    s=Solution()
    print(s.translateNum(220))