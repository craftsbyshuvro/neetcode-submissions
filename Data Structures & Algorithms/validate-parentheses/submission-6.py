class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        paranMap = {")" : "(", "}" : "{", "]" : "["}

        for index in range(len(s)):
            if s[index] in paranMap:
                if seen and paranMap[s[index]] == seen[-1]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(s[index])

        return len(seen) == 0