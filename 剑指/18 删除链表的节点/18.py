# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur != None:
            if cur.val == val:
                pre.next = cur.next
            pre = cur
            cur = cur.next
        return head

if __name__ == '__main__':
    node4=ListNode(9)
    node3=ListNode(1)
    node2 = ListNode(5)
    node1 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    s=Solution()
    print(s.deleteNode(node1,9))