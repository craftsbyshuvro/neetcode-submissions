class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        seen = {}
        while right <= (len(s) - 1):
            if s[right] not in seen:
                seen[s[right]] = right
            else:
                left = max(seen[s[right]] + 1, left)
                seen[s[right]] = right
                
            right +=1
            max_len = max(max_len, right-left)

        return max_len
