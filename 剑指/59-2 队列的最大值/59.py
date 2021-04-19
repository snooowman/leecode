# -*- coding:utf-8 -*-

import queue
class MaxQueue(object):
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self):
        """
        :rtype: int
        """
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.put(value)
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()


if __name__ == '__main__':

    s=Solution()
    print(s.isBalanced(node1))