class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_seen = []
        for num in nums:
            if num in list_seen:
                return True
            list_seen.append(num)
        return False