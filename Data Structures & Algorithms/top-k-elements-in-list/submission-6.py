class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #index will be frequency
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        placeholder = [[] for index in range(len(nums)+1)]

        for num, freq in freq.items():
            placeholder[freq].append(num)
        
        answer = []
        found = 0
        for place in reversed(placeholder):
            if len(place) != 0:
                answer.extend(place)
                found = found + 1
            if len(answer) >= k:
                return answer
        return answer
