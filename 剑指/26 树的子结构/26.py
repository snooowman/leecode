# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not A or not B:
            return False
        return self.dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def dfs(self, a, b):
        if not b:
            return True
        if not a:
            return False
        if a.val == b.val:
            return self.dfs(a.left, b.left) and self.dfs(a.right, b.right)
        else:
            return False



if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9

    node11 = TreeNode(4)
    node22 = TreeNode(8)
    node33 = TreeNode(9)
    node11.left=node22
    node11.right = node33
    s=Solution()
    print(s.isSubStructure(node1, node11))