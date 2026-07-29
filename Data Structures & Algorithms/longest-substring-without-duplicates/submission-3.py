class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        s1 = set()
        x = 0
        for r in range(len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l+=1
            s1.add(s[r])
            x = max(x,r-l+1)
        return x

            