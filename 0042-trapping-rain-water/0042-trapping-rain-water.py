class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        maxL = [0]*n
        maxR = [0]*n
        maxL[0] = height[0]
        maxR[n-1] = height[n-1]
        ans = 0
        for i in range(1, len(height)):
            maxL[i] = max(maxL[i-1], height[i])
        for j in range(n-2, -1, -1):
            maxR[j] = max(maxR[j+1], height[j])

        for k in range(len(height)):
            h = min(maxR[k], maxL[k])
            res = (h-height[k]) 
            ans += res
        return ans
        

        