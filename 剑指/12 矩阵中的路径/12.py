# -*- coding:utf-8 -*-
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def bfs(i,j,k):
            print(i,j,k)
            if not 0<=i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            ret = bfs(i-1, j, k+1) or bfs(i+1, j, k+1) or bfs(i, j-1, k+1) or bfs(i, j+1, k+1)
            board[i][j] = word[k]
            return ret

        for i in range(len(board)):
            for j in range(len(board[0])):
                if bfs(i, j, 0):
                    return True
        return False

if __name__ == '__main__':
    s=Solution()
    board = [["a", "b", "c", "e"], ["s", "f", "c", "s"], ["a", "d", "e", "e"]]
    word = "abcced"
    print(s.exist(board, word))