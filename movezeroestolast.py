class Solution():
    def moveZeroes(self, nums):
        n = len(nums)
        pointer = 0
        for i in nums:
            if i != 0:
                nums[pointer] = i
                pointer +=1

        for j in range(pointer,n):
            nums[j] = 0
        return  nums



x = Solution()
print(x.moveZeroes([0,1,0,3,12]))