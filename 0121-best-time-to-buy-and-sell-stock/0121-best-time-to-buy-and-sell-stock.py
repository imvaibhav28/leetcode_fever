class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell,profit=prices[0],prices[0],0
        length=len(prices)
        # Wait I have seen this somewhere
        # sliding window? wth min/max?
        for i in range(1,length):
            sell = prices[i] #1 to n
            if sell >= buy: #if sp>cp
            # then profit is positive
            # but if this beating the old profit?
                if sell-buy>profit: profit=sell-buy

            # elif sell>buy and sell-buy<profit: profit=profit
            else: #if sell <cp then better buy at this low price
                buy=sell
        return profit