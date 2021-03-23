# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        n = 0
        while cur.next != None:
            cur = cur.next
            n += 1
        cur = head
        for i in range(n-k+1):
            cur = cur.next
        return cur


if __name__ == '__main__':
    s=Solution()
    print(s.exchange([1,2,3,4]))