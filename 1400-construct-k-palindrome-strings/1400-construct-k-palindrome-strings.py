class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        n = len(s)
        c = 0
        for m, v in d.items():
            if v%2 != 0:
                c += 1

        if c > k:
            return False
        else:
            return True