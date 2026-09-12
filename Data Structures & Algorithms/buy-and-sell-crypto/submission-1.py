class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right <= (len(prices) - 1):
            prft = prices[right] - prices[left]
            max_profit = max(max_profit,prft)
            if prices[right] < prices[left]:
                left = right
                right +=1
            elif prices[right] > prices[left]:
                right +=1
            else:
                right +=1
        return max_profit
