class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_pro = 0

        while r < len(prices):
            # Check if profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_pro = max(profit, max_pro)
            else:
                l = r
            r+=1
        return max_pro