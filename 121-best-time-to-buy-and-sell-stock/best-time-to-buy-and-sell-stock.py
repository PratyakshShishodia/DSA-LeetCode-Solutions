class Solution(object):
  def maxProfit(self, prices):
    i = 0
    max_profit = 0
    for j in range(i,len(prices)):
         if prices[j] < prices[i] :
            i = j
         else:
            profit = prices[j]-prices[i]
         max_profit = max(max_profit, profit)
    return max_profit

        