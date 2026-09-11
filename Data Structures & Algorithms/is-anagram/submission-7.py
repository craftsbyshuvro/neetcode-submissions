class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        first = {}
        second = {}
        for i in range(len(s)):
            if s[i] in first:
                first[s[i]] = first[s[i]] + 1
            else:
                first[s[i]] = 1

            if t[i] in second:
                second[t[i]] = second[t[i]] + 1
            else:
                second[t[i]] = 1
        
        return first == second