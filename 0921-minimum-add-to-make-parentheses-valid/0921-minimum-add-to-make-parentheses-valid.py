class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                st.append(s[i])
            elif s[i] == ")":
                if st:
                    st.pop()
                else:
                    res += 1
        return res+len(st)