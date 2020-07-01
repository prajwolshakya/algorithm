class Solution():
    def productExceptSelf(self, nums):
        curr = 1
        result = []
        for num in nums:
            result.append(curr)
            curr *= num
        curr = 1
        print(result)
        for i in range(len(nums) - 1, -1, -1):
            print(curr)
            result[i] *= curr
            curr *= nums[i]

        return result
    #
    # x = len(nums)
    # op = [0] * x
    # p = 1
    # for i in range(0, x):
    #     p = p * nums[i]
    #     op[i] = p
    # p = 1
    # for i in range(x - 1, 0, -1):
    #     # if i == x-1:
    #     #     op[i] = op[i-1]
    #     #     p *= nums[i]
    #     # elif i == 0:
    #     #     op[i] = p
    #     # else:
    #     op[i] = p * op[i - 1]
    #     p *= nums[i]
    # op[0] = p
    #
    # return op

x =  Solution()
print(x.productExceptSelf([1,2,3,4]))