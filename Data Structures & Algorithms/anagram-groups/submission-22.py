from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for strVal in strs:
            count = [0] * 26
            for val in strVal:
                count[ord(val) - 97] += 1
            result[tuple(count)].append(strVal)

        return list(result.values())