class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            elif nums[m] > nums[r]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m+1
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m
            else:
                r -=1
        return nums[l] == target