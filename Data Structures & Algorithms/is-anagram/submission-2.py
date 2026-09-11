class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        first = list(s)
        
        for item in list(t):
            if item not in first:
                return False
            else:
                first.remove(item)
        return True
