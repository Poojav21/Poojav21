class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        st = []
        d = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                while not st or st[-1] != d[i]:
                    return False
                st.pop()
            
        while st:
            return False
        return True