# -*- coding:utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = float("+inf")
        money = 0
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            else:
                money = max(price - lowest_price, money)
        return money


if __name__ == '__main__':
    s=Solution()
    print(s.maxProfit([7,6,4,3,1]))