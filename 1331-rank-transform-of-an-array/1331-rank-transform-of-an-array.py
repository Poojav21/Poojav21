class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = sorted(set(arr))

        d = {}
        for i in range(len(l)):
            d[l[i]] = i+1
        res = []
        for num in arr:
            res.append(d[num])
        return res
        