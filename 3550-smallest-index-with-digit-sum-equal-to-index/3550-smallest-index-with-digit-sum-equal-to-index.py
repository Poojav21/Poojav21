class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumofdigit(num):
            s = 0
            while num > 0:
                b = num%10
                s += b
                num = num//10
            return s
        for i in range(len(nums)):
            m = sumofdigit(nums[i])
            if m == i:
                return i
        return -1

