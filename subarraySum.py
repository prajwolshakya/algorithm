class Solution():
    def subarraySum(self, nums, k):
        l = len(nums)
        result, s = 0,0
        d = {0:1}
        for i in range(0,l):
            s += nums[i]
            if s-k in d:
                result += d[s-k]
            d[s] = d.get(s,0) +1
        return  result




x = Solution()
print(x.subarraySum([1,1,1],2))