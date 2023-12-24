def maxProfit(prices):
    left, right = 0, 1 # left = buy, right = sell
    maxProfit = 0
    while (right < len(prices)):
        if (prices[left] < prices[right]):
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1
    return maxProfit
prices = list(map(int, input("Enter prices: ").split()))
maxProfit(prices)