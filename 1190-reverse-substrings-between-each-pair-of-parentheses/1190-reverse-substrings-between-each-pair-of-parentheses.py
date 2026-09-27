class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] == "(":
                st.append(s[i])
            elif s[i] == ")":
                temp = []
                while st and st[-1] != "(":
                    temp.append(st.pop())
                st.pop()
                st.extend(temp)
            else:
                st.append(s[i])
        return "".join(st)


        