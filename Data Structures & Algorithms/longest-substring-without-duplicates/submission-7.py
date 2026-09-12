class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = {}
        max_len = 0
        while right <= (len(s) - 1):
            if s[right] not in seen:
                seen[s[right]] = right
                right +=1
            else:
                left = max(left, seen[s[right]] + 1)
                seen[s[right]] = right
                right +=1
            
            max_len = max(max_len, right-left)
        return max_len