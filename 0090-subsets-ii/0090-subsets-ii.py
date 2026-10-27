class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def sub(i, nums ,ans, l):

            ans.append(l[:])
       
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                l.append(nums[j])
                sub(j+1, nums, ans, l)
                l.pop()

            return ans
        nums.sort()
        return sub(0, nums, [], [])
        