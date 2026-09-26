class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        def min_days(bloomDay, mid, k):
            count = 0
            ans = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    count += 1
                else:
                    ans += count//k
                    count = 0
            ans += count//k
            return ans
            
        l = min(bloomDay)
        r = max(bloomDay)
        ans = -1
        while l <= r:
            mid = (l+r)//2
            res = min_days(bloomDay, mid, k)
            if res >= m:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
