class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                c = s[i:j]
                if c == c[::-1]:
                    res += 1
        return res
        