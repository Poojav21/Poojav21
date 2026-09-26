class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        arr = sorted(position)
        # code here
        def cows(arr, k , m):
            count = 1
            lastcow = arr[0]
            for i in range(len(arr)):
                if arr[i] - lastcow >= k:
                    count += 1
                    lastcow = arr[i]
            if count >= m:
                return True
            return False
        
        n = len(arr)
        l = 0
        r = arr[n-1] - arr[0]

        while l <= r:
            k = (l+r)//2
            ans = cows(arr, k, m)
            if ans is True:
                l = k+1
            else:
                r = k-1
        return r
        