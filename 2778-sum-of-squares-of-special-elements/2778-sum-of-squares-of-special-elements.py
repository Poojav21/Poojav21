class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                print(nums[i])
                s += nums[i]**2
        return s