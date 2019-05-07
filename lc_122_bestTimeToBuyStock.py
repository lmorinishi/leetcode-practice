class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) is 1:
            return 0

        y = [prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1]]
        return sum(y)
