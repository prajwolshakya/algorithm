class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def compare(s):
            ans = []
            for i in s:
                if(i != "#"):
                    ans.append(i)
                else:
                    ans.pop()
            return ''.join(ans)
        return compare(S) == compare(T)
                    


l = Solution()
print(l.backspaceCompare("ab#c","ad#c"))
print(l.backspaceCompare("a#c","b"))

