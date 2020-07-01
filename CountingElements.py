class Solution():
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
	count = 0
	for i in range(0,len(arr)):
		x = 0
		x = arr[i] + 1
		if x in arr:
			count +=1
			#print(count)
	return count
		
		
	

		


a = [[1,2,3],[1,1,3,3,5,5,7,7],[1,3,2,3,5,0],[1,1,2,2]]
x = Solution()
for i in a:
	print(x.countElements(i))
print("end of for")
print(x.countElements([1,3,2,3,5,0]))
