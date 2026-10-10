class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        n = len(s)
        e = 0
        o = 0
        for k, v in d.items():
            if v%2 != 0:
                o += 1
        if o == 0:
            return n
        else:
            return n-o+1


           