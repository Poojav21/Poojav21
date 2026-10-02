# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l+r)//2
            bd = isBadVersion(m)
            if bd == True:
                r = m-1
            else:
                l = m+1
        return l