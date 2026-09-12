class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalHours(piles, i):
            total_hours = 0
            for k in piles:
                total_hours += math.ceil(k/i)
            return total_hours
        res = float('inf')
        l = 1
        r = max(piles)
        while l<=r:
            m = (l+r)//2
            total_hours = totalHours(piles, m)
            if total_hours <= h:
                res = min(res , m)
                r = m-1
            else:
                l = m+1
        return res
        