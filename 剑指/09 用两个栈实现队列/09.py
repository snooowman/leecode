# -*- coding:utf-8 -*-
class CQueue(object):

    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.A.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.A == []:
            return -1
        self.B = self.A[::-1]
        ret = self.B[len(self.A) - 1]
        self.B.pop(len(self.A)-1)
        self.A = self.B[::-1]
        return ret




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


if __name__ == '__main__':
    s=Solution()
    print(s.buildTree(preorder,inorder))
    print(preorder[1:1])