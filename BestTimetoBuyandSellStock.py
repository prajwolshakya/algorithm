import math
class Solution():

    def maxProfit(self, prices):
        best_without_stock,best_with_stock = 0, -math.inf
        for i in range(0,len(prices)):
            print(prices[i])
            print('B best_with_stock'+str(best_with_stock))

            best_with_stock = max(best_with_stock,best_without_stock-prices[i])
            print('A best_with_stock'+str(best_with_stock))
            print('B best_without_stock'+str(best_without_stock))
            best_without_stock = max(best_without_stock,best_with_stock+ prices[i])
            print('A best_without_stock'+str(best_without_stock))


        return  best_without_stock


x = Solution()
print(x.maxProfit([1,2,3,4,5]))

