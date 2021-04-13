# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = []
        queue.append(root)
        while queue:
            temp = []
            for i in queue:
                left = right = 0
                if i.left:
                    temp.append(i.left)
                    left = self.maxdep(i.left)
                if i.right:
                    temp.append(i.right)
                    right = self.maxdep(i.right)
                if abs(left - right) > 1:
                    return False
            queue = temp
        return True

    def maxdep(self, root):
        if not root:
            return 0
        return max(self.maxdep(root.left), self.maxdep(root.right)) + 1

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(3)
    node6 = TreeNode(4)
    node7 = TreeNode(4)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    node4.left = node6
    node5.right = node7
    s=Solution()
    print(s.isBalanced(node1))