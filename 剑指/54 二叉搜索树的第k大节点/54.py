# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = []
        self.midScan(l, root)
        print(l)
        return l[len(l)-k]


    def midScan(self, l, root):
        if root.left:
            self.midScan(l, root.left)
        l.append(root.val)
        if root.right:
            self.midScan(l, root.right)


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(4)
    node4 = TreeNode(2)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    s=Solution()
    print(s.kthLargest(node1,1))