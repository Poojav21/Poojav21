class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def sub(i, nums ,ans, l):
            if i == len(nums):
                ans.append(l[:])
                return 
            l.append(nums[i])
            sub(i+1, nums, ans, l)
            l.pop()
            sub(i+1, nums, ans, l)
            return ans
        return sub(0, nums, [], [])