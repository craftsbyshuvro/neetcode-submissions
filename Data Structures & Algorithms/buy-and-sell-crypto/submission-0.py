class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right <= (len(prices) - 1):
            prft = prices[right] - prices[left]
            profit = max(prft, profit)

            if prices[left] > prices[right]:
                left = right
                right +=1
            else:
                right +=1
        return profit
