import collections
class Solution():
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = 0
        d = {}
        ans = collections.defaultdict(list)
        for i in strs:
            ans[tuple(sorted(i))].append(i)
            # print(tuple(sorted(i)),i)
        return ans


x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# class Solution(object):
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
#         return ans.values()
