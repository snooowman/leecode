# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # cur = head
        # List = []
        # if cur:
        #     while cur.next:
        #         List.append(cur.val)
        #         cur = cur.next
        #     List.append(cur.val)
        #     List = List[::-1]
        #     res = ListNode(List[0])
        #     cur = res
        #     for i in range(1, len(List)):
        #         l = ListNode(List[i])
        #         cur.next = l
        #         cur = cur.next
        #     return res
        # else:
        #     return head

        # 迭代
        cur = head
        if cur:
            pre = None
            while cur.next:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        else:
            return head


if __name__ == '__main__':
    node5 = ListNode(5)
    node4 = ListNode(4)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    s=Solution()
    print(s.reverseList(node1))