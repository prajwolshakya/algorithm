def remove(nums):
     i,array = 0,[]
     while i < len(nums):
             x = nums[i]
             if x not in array:
                     array.append(x)
             i = i+1
     return len(array)

print(remove([1,2,2]))
