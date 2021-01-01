# -*- coding:utf-8 -*-
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.replace(' ', '%20')



if __name__ == '__main__':
    s=Solution()
    s1 = "We are happy."
    print s.replaceSpace(s1)