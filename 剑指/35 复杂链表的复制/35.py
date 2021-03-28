# -*- coding:utf-8 -*-
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ## 哈希表
        # dic = {}
        # cur = head
        # while cur:
        #     dic[cur] = Node(cur.val)
        #     cur = cur.next
        # cur = head
        # while cur:
        #     dic[cur].next = dic.get(cur.next)
        #     dic[cur].random = dic.get(cur.random)
        #     cur = cur.next
        # return dic[head]

        ## dfs
        def dfs(head):
            if not head:
                return None
            if head in visited:
                return visited[head]
            else:
                visited[head] = Node(head.val)
                visited[head].next = dfs(head.next)
                visited[head].random = dfs(head.random)
                return visited[head]
        visited = {}
        return dfs(head)



if __name__ == '__main__':
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    s=Solution()
    print(s.copyRandomList(node1))