# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        temp = TreeNode(0)
        if not root:
            return root
        if root.left or root.right:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root

if __name__ == '__main__':
    s=Solution()
    print(s.exchange([1,2,3,4]))