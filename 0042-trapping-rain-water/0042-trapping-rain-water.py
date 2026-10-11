class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxL = [0]*n
        maxR = [0]*n
        maxL[0] = height[0]
        maxR[n-1] = height[n-1]
        for i in range(1, n):
            maxL[i] = max(height[i], maxL[i-1])
        for j in range(n-2, -1, -1):
            maxR[j] = max(height[j], maxR[j+1])
        ans = 0
        for k in range(n):
            print(maxL[k])
            diff = min(maxL[k], maxR[k])
            ans += diff - height[k] 
        return ans