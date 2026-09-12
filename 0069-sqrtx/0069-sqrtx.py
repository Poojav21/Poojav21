class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x-1
        res = 0
        if x == 1 or x == 0:
            return x
        while l <= r:
            m = (l+r)//2
            if m*m <= x:
                res = m
                l = m+1
            else:
                r = m-1
        return res
        