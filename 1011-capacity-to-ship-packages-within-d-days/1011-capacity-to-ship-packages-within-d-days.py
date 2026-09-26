class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def daysReq(weights, m):
            days = 1
            load = 0
            for i in weights:
                if load + i > m:
                    days = days+1
                    load = i
                else:
                    load += i
            return days
        l = max(weights)
        r = sum(weights)
        res = float('inf')
        while l <= r:
            m = (l+r)//2
            d = daysReq(weights, m)
            if d <= days:
                res  = min(res, m)
                r = m-1
            else:
                l = m+1
        return res