# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 and l2:
        #     if l1.val > l2.val:
        #         l = cur = l2
        #         l2 = l2.next
        #     else:
        #         l = cur = l1
        #         l1 = l1.next
        #     while l1 and l2:
        #         if l1.val > l2.val:
        #             cur.next = l2
        #             l2 = l2.next
        #         else:
        #             cur.next = l1
        #             l1 = l1.next
        #         cur = cur.next
        #     cur.next = l1 if l1 else l2
        #     return l
        # else:
        #     return l1 if l1 else l2

        # 伪头节点
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next, l2 = l2, l2.next
            else:
                cur.next, l1 = l1, l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next

if __name__ == '__main__':
    s=Solution()
    print(s.exchange([1,2,3,4]))