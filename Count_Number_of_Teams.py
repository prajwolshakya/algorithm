class Solution:
	def numTeams(self, r):
		b = []

		for i in range(0,len(r)-1):
			for j in range(1,len(r)):
				for k in range(2,len(r)):
					if( i<j<k and r[i] < r[j] < r[k] or  i<j<k and r[i] >r[j] > r[k]):
						b.append((r[i],r[j],r[k]))
		print(b)

		while i < len(r)-1:
			j = i+1
			while j < len(r):
				k = j+1
				while k < len(r):
					print('i'+str(i))
					print(j)
					print(k)
					if (i < j < k and r[i] < r[j] < r[k] or i < j < k and r[i] > r[j] > r[k]):
					    b.append((r[i],r[j],r[k]))
					k =  k + 1
				j= j+1
			i= i+1
		return b
x = Solution()
print(x.numTeams([1,2,3,4]))
