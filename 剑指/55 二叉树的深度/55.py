# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

        #BFS
        queue = []
        queue.append(root)
        res = 0
        while queue:
            temp = []
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp
            res += 1
        return res

if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    s=Solution()
    print(s.maxDepth(node1))