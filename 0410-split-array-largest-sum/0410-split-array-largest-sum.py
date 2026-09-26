class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        if len(nums) < k:
            return -1
        def allocatePage(nums, k , m):
            count = 1
            pages = 0
            for page in nums:
                if page + pages > m:
                    count += 1
                    pages = page
                else:
                    pages += page
            if count <= k:
                return True
            else:
                return False
        
        
        l = max(nums)
        r = sum(nums)
        ans = float('inf')
        while l <= r:
            m = (l+r)//2
            pages = allocatePage(nums, k , m)
            if pages:
                ans = min(ans, m)
                r = m-1
            else:
                l = m+1
        return ans
        
        