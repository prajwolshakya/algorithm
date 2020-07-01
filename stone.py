import heapq
class Solution():
    def lastStoneWeight(self, stones):
        a,s = [],len(stones)
        for i in range(s):
            stones[i] =-stones[i]
        stones.sort()
        while s >= 2:
            print('pop',stones)
            y = -stones.pop(0)
            x = -stones.pop(0)
            print('x',x)
            print('y',y)
            if x == y:
                s -= 2
            else:
                s -= 1
                ans = -(y-x)
                stones.append(ans)
                stones.sort()
            print('After pop',stones)
        if s == 0:
            return 0
        return -stones.pop()


 
x = Solution()
print(x.lastStoneWeight([1,2,3,6,7]))
