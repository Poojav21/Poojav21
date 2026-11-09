class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxL = [height[0]]*n
        maxR = [height[n-1]]*n
        for i in range(1, n):
            maxL[i] = max(height[i], maxL[i-1])
        for j in range(n-2,-1,-1):
            maxR[j] = max(height[j], maxR[j+1])
        c = 0
        for k in range(n):
            diff = min(maxL[k], maxR[k])
            width = diff - height[k]
            c += width
        return c