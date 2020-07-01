class Solution():
    def isHappy(self, n):
        for i in range(0,20):
           n = self.calc(n)
           # print(n)
           if n == 1:
               return True
        return False
    def calc(self,n):
        sum = 0
        while n:
            d = n %10
            n = n/10
            sum += d*d
        return sum



x = Solution()
print(x.isHappy(3))