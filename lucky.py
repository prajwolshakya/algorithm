class Solution:
    def findLucky(self, arr):
        # d = {}
        # for i in arr:
        #     if i in d.keys():
        #         d[i] =  d[i]+1
        #     else:
        #         d[i] = 1
        # print(d)
        # for (key, value) in d.items():
        #     if value ^ key == 0:
        #         return key
        # ans = 0
        # a = 0
        # for i in arr:
        #     a = a+i
        #     # print(ans)
        #     ans = max(ans,a)
        #     a = max(a,0)
        #
        # return  ans
        n = len(arr)
        a = [0] * n
        min_so_far = 0
        ans = 0
        for i in range(0,n):
          a[i] = arr[i] + ( 0 if  i == 0 else a[i-1])
        print(a)
        for j in range(0,n):
            if(min_so_far != 0):
                ans = max(ans,a[j]-min_so_far)
            min_so_far = min(min_so_far,a[j])
            print(min_so_far)
        return ans

x = Solution()
print(x.findLucky([-1]))
# 19,12,11,14,18,8,6,6,13,9,8,3,10,10,1,10,5,12,13,13,9