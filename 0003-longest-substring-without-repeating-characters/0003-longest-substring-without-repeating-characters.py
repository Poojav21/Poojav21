class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        d = {}
        while j < len(s):
            
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1

            if len(d) == j-i+1:
                ans = max(ans, j-i+1)
                j += 1
            else:
                while len(d) < j-i+1:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        del d[s[i]]
                    i +=1
                j += 1
        return ans

        