class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for p in range(1,len(prices)):
            if prices[p]>prices[p-1]:
                res+=prices[p]-prices[p-1]
        return res