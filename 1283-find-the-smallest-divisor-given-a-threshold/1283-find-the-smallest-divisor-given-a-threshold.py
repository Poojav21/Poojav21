import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def smallest_divisor(nums, m):
            s = 0
            for i in nums:
                s += math.ceil(i/m)
            return s
        l = 1
        r = max(nums)

        res = float('inf')
        while l <= r:
            m = (l + r)//2
            su = smallest_divisor(nums, m)
            if su <= threshold:
                res = min(m , res)
                r = m-1
            else:
                l = m+1
        return res
        