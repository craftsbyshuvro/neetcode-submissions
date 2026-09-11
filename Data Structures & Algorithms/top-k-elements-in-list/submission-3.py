class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        palceholder = [[] for index in range(len(nums) + 1)]

        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for item in freq.items():
            palceholder[item[1]].append(item[0])
        
        count = 0
        answer = []
        for place in list(reversed(palceholder)):
            if len(place) > 0:
                answer.extend(place)
                count = count + 1
            
            if len(answer) == k:
                return answer
        return answer
            

