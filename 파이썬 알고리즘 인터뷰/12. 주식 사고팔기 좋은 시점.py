# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		minPrices = prices[0] + 1
		maxProfit = 0
		for i in range(len(prices)):
			if minPrices > prices[i]:
				profit = max(prices[i:]) - prices[i]
				maxProfit = profit if profit > maxProfit else maxProfit
				minPrices = prices[i]
		return maxProfit

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		min_price = sys.maxsize
		for price in prices:
			min_price = min(min_price, price)
			profit = max(profit, price - min_price)
		return profit
