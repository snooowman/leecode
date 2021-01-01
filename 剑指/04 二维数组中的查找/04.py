# -*- coding:utf-8 -*-
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #从右上角开始
        if matrix == []:
            return False
        row = 0
        col = len(matrix[0])-1
        while(row<len(matrix) and col >=0):
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                print 1
                return True
        print 2
        return False

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] < target:
        #             pass
        #         elif matrix[i][j] == target:
        #             return True
        #         else:
        #             break
        # return False

if __name__ == '__main__':
    s=Solution()
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    s.findNumberIn2DArray(m, 20)