class Solution():
    def rangeBitwiseAnd(self, m, n):
        ans = 0
        c = 0
        for i in range(30,-1,-1):
            if (m & (1 << i)) != (n & (1 << i)):
                break
            else:
               ans |= (m & (1 << i))
        print(ans)
        if m != n:
            m >>=1
            n >>=1
            c += 1
        print(m<<c)

x =Solution()
print(x.rangeBitwiseAnd(5,7))
