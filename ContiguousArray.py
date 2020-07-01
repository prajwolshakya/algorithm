class Solution():
    def findMaxLength(self, nums):
        d = {}
        d[0]=0
        n,ans,pre = len(nums),0,0
        for i in range(n):
            pre += (-1 if nums[i] == 0 else 1) #example 0,-1,0,-1
            if pre in d:
                ans = max(ans,i + 1 - d[pre])
            else:
                d[pre] = i+1
        return ans
x = Solution()
print(x.findMaxLength([0,1]))
