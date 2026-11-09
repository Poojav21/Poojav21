class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                c = s[i:j]
                if c == c[::-1] and len(c) > len(res):
                    res = c
        return res