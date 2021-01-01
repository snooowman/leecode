class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = -1
        set1 = set()
        for i in range(len(nums)):
            set1.add(nums[i])
            if len(set1) < i+1:
                print nums[i]
                return nums[i]


if __name__ == '__main__':
    s=Solution()
    s.findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 99])