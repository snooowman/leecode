# -*- coding:utf-8 -*-
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        res = []
        length = len(matrix) if len(matrix)<len(matrix[0]) else len(matrix[0])
        l = int(length/2)+1 if length%2 else int(length/2)
        for i in range(l):
            j = k = o = 0
            for j in range(len(matrix[i])-2*i):
                res.append(matrix[i][i + j])
            if len(matrix[i]) - 2 * i == 0:
                return res

            for k in range(len(matrix) - 2*i -1):
                res.append(matrix[1 + i + k][i + j])
            if len(matrix) - 2 * i - 1 == 0:
                return res

            for o in range(len(matrix[i]) - 2*i -1):
                res.append(matrix[1 + i + k][i + j - o - 1])
            if len(matrix[i]) - 2 * i - 1 == 0:
                return res

            for p in range(len(matrix) - 2*i -2):
                res.append(matrix[1 + i + k - 1 - p][i + j - o - 1])
            if len(matrix) - 2 * i - 2 == 0:
                return res
        return res


if __name__ == '__main__':
    matrix = [[2,5],[8,4],[0,-1]]
    s=Solution()
    print(s.spiralOrder(matrix))