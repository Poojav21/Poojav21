class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {")": "(", "}":"{", "]":"["}
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st  or st[-1] != d[i]:
                    return False
                st.pop()
        return len(st) == 0
                