class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s1 = {}
        s2 = {}

        for ch in s:
            if ch not in s1:
                s1[ch] = 1
            else:
                s1[ch] += 1
        
        for ch in t:
            if ch not in s2:
                s2[ch] = 1
            else:
                s2[ch] += 1
        
        for n in s1:
            if n not in s2:
                return False
            if s1[n] != s2[n]:
                return False

        return True