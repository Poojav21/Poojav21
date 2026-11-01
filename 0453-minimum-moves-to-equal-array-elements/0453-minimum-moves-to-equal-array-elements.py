class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        m = min(nums)
        # print(m)
        for i in nums:
            b = i-m
            print("b",b)
            c += b
        return c
        