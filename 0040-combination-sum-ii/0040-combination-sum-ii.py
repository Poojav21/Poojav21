class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combinationsum(i, candidates, target, ans, l):
            if target == 0:
                ans.append(l[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > target:
                    break
                else:
                    l.append(candidates[j])
                    combinationsum(j+1, candidates, target-candidates[j], ans, l)
                    l.pop()
            return ans
        candidates.sort()
        a = combinationsum(0, candidates, target, [], [])
        return a
        