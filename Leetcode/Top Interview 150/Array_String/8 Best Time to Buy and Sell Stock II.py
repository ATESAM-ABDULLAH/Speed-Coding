def maxProfit(prices):
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.

    :type prices: List[int]
    :rtype: int
    """
    diff = [
        prices[i + 1] - prices[i] for i in range(len(prices) - 1)
    ]  # diffrence in price per day
    profit = sum([x for x in diff if x > 0])  # sum only +ve days i.e profitable days
    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
