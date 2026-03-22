#Best Time to Buy and Sell Stock I

# class Solution(object):
#     def maxProfit(self, prices):
#         maxP=0
#         cheapest=prices[0]
#         # track the minimum price from left and cal max based on it, if anything less exists later replace cheapest with it
#         for i in range(1,len(prices)):
#             if prices[i]<cheapest:
#                 cheapest=prices[i]
#             else:
#                 maxP=max(maxP,prices[i]-cheapest)
#         return maxP


#Best Time to Buy and Sell Stock II

class Solution(object):
  
    def maxProfit(self, prices):
          profit=0
          buy=prices[0]

          for i in range(1,len(prices)):
                # IF  BOUGHT STOCK HAS GREATER PRICE THAN CURRENT STOCK, BUY THE CHEAPER ONE AND IF CURRENT STOCK HAS GREATER VALUE THAN bOUGHT, SELL AND REBUY THE CURRENT ONE as On each day, you may decide to buy and/or sell the stock
                if prices[i]>buy:
                     profit+=prices[i]-buy
                buy=prices[i]
          return profit


print(Solution().maxProfit([7,1,5,3,6,4]))