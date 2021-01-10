# -*- coding:utf-8 -*-
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers) == 1:
            print(numbers[0])
            return numbers[0]
        left = 0
        right = len(numbers)-1
        while left < right:
            mid = left + int((right - left) / 2)
            if numbers[right] > numbers[mid]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                right -= 1
        return numbers[left]

if __name__ == '__main__':
    s=Solution()
    print(s.minArray([3,4,5,1,2]))