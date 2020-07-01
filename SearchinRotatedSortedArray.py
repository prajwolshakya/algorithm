class Solution():
    def search(self, nums, target):
        l = 0
        r = len(nums) -1
        first = nums[0]
        while l <= r:
            m =  int(l + (r-l)/2)
            value = nums[m]
            if value == target:
               return m
            an_big = value>=first
            target_big = target>= first
            if target_big == an_big:
                if value < target:
                    l = m+1
                else:
                    r = m-1
            else:
                if an_big:
                    l = m+1
                else:
                    r = m-1






            # if nums[m] > nums[r]:
            #     l = m+1
            # else:
            #     r = m
        # print(l,r)
        # s = l
        # l = 0
        # r = len(nums) - 1
        #
        # if target >= nums[s] and target <= nums[r]:
        #     l = s
        # else:
        #     r = s
        # print(l, r)
        # while l<= r:
        #     m = int(l + (r - l) / 2)
        #
        #     if target == nums[m]:
        #         return  m
        #     elif nums[m] < target:
        #         l = m +1
        #     else:
        #         r = m-1
        # return  -1

    # l, r = 0, len(nums) - 1
    #
    # while l <= r:
    #     m = (l + r) // 2
    #
    #     if nums[m] == target:
    #         return m
    #     elif nums[m] >= nums[l]:
    #         if target >= nums[l] and target < nums[m]:
    #             r = m - 1
    #         else:
    #             l = m + 1
    #     else:
    #         if target > nums[m] and target <= nums[r]:
    #             l = m + 1
    #         else:
    #             r = m - 1
    #
    # return -1




x = Solution()


print(x.search([4,5,6,7,0,1,2],0))