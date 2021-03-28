# -*- coding:utf-8 -*-
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        return self.helper(postorder, 0, len(postorder)-1)

    def helper(self, postorder, left, right):
        if left >= right:
            return True
        i = left
        while postorder[i] < postorder[right]:
            i += 1
        for j in range(i,right):
            if postorder[j] < postorder[right]:
                return False
        return self.helper(postorder, left, i-1) and self.helper(postorder, i, right-1)


if __name__ == '__main__':
    s=Solution()
    print(s.verifyPostorder([1,2,5,10,6,9,4,3]))