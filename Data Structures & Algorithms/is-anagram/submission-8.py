class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False     
        string1 = {}
        for val in s:
            if val in string1:
                string1[val] = string1[val] + 1
            else:
                string1[val] = 1

        string2 = {}
        for val in t:
            if val in string2:
                string2[val] = string2[val] + 1
            else:
                string2[val] = 1
        return string1 == string2