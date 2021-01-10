# -*- coding:utf-8 -*-
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        self.board = [[0 for x in range(n)] for y in range(m)]
        def dfs(a, b):
            if (not 0 <= a < m) or (not 0 <= b < n) or (int(a/10) + a%10 +int(b/10) + b%10 > k) or (self.board[a][b] == 1):
                return 0
            self.board[a][b] = 1
            return 1 + dfs(a+1,b)+dfs(a, b+1)+dfs(a-1, b)+dfs(a, b-1)
        return dfs(0,0)

if __name__ == '__main__':
    s=Solution()
    print(s.movingCount(1,2, 1))