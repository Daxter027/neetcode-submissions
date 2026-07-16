class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices, reverse = True) == prices:
            return 0
        
        i = 0
        j = 1
        maxx = 0
        while j<len(prices):
            
            if prices[i]<prices[j]:
                diff = prices[j]-prices[i]
                maxx = max(maxx,diff)
                j+=1
            else:
                i = j
                j+=1
        return maxx

                


