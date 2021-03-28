# -*- coding:utf-8 -*-
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(s, path, used):
            if len(path) == len(s):
                res.append(''.join(path))
                return
            for i in range(len(s)):
                if used[i] == False:
                    if i>=1 and s[i-1]==s[i] and used[i-1]==False:
                        continue
                    path.append(s[i])
                    used[i] = True
                    backtrack(s,path, used)
                    used[i] = False
                    path.pop(-1)

        if len(s) == 0:
            return []
        temp = []
        l = list(s)
        l.sort()
        s = ''.join(l)
        used = []
        for i in range(len(l)):
            used.append(False)
        res = []
        backtrack(l, temp, used)
        return res




if __name__ == '__main__':
    s=Solution()
    print(s.permutation('abc'))