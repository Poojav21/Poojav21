class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        i = 0
        j = 0
        res = 0
        while j < len(s):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            if len(d) == j-i+1:
                res = max(res, j-i+1)
                j += 1
            else:
                while len(d) < j-i+1:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        del d[s[i]]
                    i += 1
                j += 1
        return res
