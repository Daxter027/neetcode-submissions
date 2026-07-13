class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1 = {}
        d2 = {}

        for i in s:
            d1[i] = s.count(i)
        for i in t:
            d2[i] = t.count(i)

        for i in d1:
            if i not in d2:
                return False
            elif d1[i] != d2[i]:
                return False
        return True