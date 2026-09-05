class Solution:
    def buysellstock(self,prices):
        min_prices=prices[0]
        max_profit=0
        for price in prices:
            if price<min_prices:
                min_prices=price
            else:
                profit= price-min_prices
		
            if profit>max_profit:
                max_profit=profit
        return max_profit
	
prices = [7, 1, 5, 3, 6, 4]
obj=Solution()
print(obj.buysellstock(prices))
	


      
