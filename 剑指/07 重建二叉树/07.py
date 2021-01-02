# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        #切片表示第几个，而不是下标是几
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root


if __name__ == '__main__':
    s=Solution()
    print(s.buildTree(preorder,inorder))
    print(preorder[1:1])