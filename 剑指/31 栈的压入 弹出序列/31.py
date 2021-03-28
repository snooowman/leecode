# -*- coding:utf-8 -*-
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # if not pushed:
        #     return True
        # stack = [pushed[0]]
        # pushnum = 1
        # for i in popped:
        #     if stack:
        #         while stack[-1] != i:
        #             if pushnum > len(pushed)-1:
        #                 return False
        #             stack.append(pushed[pushnum])
        #             pushnum+=1
        #         stack.pop()
        #     else:
        #         stack.append(pushed[pushnum])
        #         pushnum+=1
        #         while stack[-1] != i:
        #             if pushnum > len(pushed)-1:
        #                 return False
        #             stack.append(pushed[pushnum])
        #             pushnum+=1
        #         stack.pop()
        # return True
        stack = []
        num = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[num]:
                stack.pop()
                num += 1
        return not stack


if __name__ == '__main__':
    s=Solution()
    print(s.validateStackSequences([1,3,2,0],[1,2,0,3]))