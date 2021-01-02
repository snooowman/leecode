# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(3)
l1.next=l2
l3 = ListNode(2)
l2.next=l3

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s[::-1]


if __name__ == '__main__':
    s=Solution()
    print(s.reversePrint(l1))