class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combinationsum(i, candidates, target, ans, l):
            if i == len(candidates):
                if target == 0:
                    ans.append(l[:])
                return
            if candidates[i] <= target:
                l.append(candidates[i])
                combinationsum(i, candidates, target-candidates[i], ans, l)
                l.pop()
            combinationsum(i+1, candidates, target, ans, l)
            return ans
        return combinationsum(0, candidates, target, [], [])
            

        