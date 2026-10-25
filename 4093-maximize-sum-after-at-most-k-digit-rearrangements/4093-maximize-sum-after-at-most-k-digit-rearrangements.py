class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(nums)
        gains = []
        for num in nums:
            rearr = int("".join(sorted(str(num), reverse=True)))
            gains.append(rearr-num)
        gains.sort(reverse = True)
        return total+sum(gains[:k])









        # nums.sort()
        # for i in range(k):
        #     s = str(nums[i])
        #     nums[i] = int("".join(sorted(s, reverse = True)))
        # return sum(nums)
            
        