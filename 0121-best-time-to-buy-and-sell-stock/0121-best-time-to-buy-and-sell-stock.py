class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for price in prices[1:]:
            # if current loop 'price' is higher than previously bought price and
            # expected profit is highter than current profit,
            # replace current profit with expected profit.
            if buy < price and (price - buy) > profit:
                profit = price - buy
            # if current loop 'price' is lower than previously bought price,
            # update bought price
            if buy > price:
                buy = price
        
        return profit
            