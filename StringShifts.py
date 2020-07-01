class Solution():
    def stringShift(self, s, shift):
        l= len(s)
        for i in shift:
           if i[0] == 1:
              s= s[l - i[1]:l] + s[0:l - i[1]]
           else:
              s= s[i[1]:l] + s[0:i[1]]
        return s




x = Solution()
print(x.stringShift("xqgwkiqpif",[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))