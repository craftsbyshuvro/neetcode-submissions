class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        e_val = []
        for num in nums:
            if num in e_val:
                return True
            e_val.append(num)
        return False