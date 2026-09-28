class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                st.append(s[i])
                res = max(res, len(st))
            elif s[i] == ")":
                st.pop()


        return res
                