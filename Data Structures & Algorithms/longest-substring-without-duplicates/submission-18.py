class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        seen = set()

        while right <= (len(s) -1):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left +=1
                seen.add(s[right])
                
            right +=1
            max_len = max(max_len, len(seen))
        return max_len