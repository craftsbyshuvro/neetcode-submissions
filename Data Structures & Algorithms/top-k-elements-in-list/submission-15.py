class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        counterR = [[] for _ in range(len(nums)+1)]

        for key in freq:
            counterR[freq[key]].append(key)
        
        result = []
        for item in range(len(counterR) -1, -1, -1):
            if len(counterR[item]) != 0:
                result.extend(counterR[item])
                if len(result) == k:
                    break
        
        return result
        
