class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0
        while(r < len(prices)):
          if prices[l] < prices[r]:
             profit =prices[r] - prices[l]
             maxp= max(maxp,profit)
          else:
             l = r

          r = r + 1
        return maxp 
                 
                
## Hume isme Find karna hai lowest buying and highest selling, so two points to go ,and therefore we do the two pointer algo here, 
