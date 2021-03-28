# -*- coding:utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        temp = []
        temp.append(root)
        while temp:
            node = temp.pop(0)
            res.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        return res


if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node1.right = node2
    s=Solution()
    print(s.levelOrder(node1))