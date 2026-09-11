class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}
        for index in range(len(numbers)):
            diff = target - numbers[index]
            if diff in freq:
                return [freq[diff]+1,index+1]
            freq[numbers[index]] = index
        return []