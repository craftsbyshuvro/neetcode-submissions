import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        
        for num, value in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, num))
            else:
                heapq.heappushpop(heap, (value, num))
        
        answer = [item[1] for item in heap]
        return answer