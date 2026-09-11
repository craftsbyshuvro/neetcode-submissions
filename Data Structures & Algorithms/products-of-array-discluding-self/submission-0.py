class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for index, num in enumerate(nums):
            current_pro = 1
            for inindex, innum in enumerate(nums):
                if index != inindex:
                    current_pro = current_pro * innum
            output.append(current_pro)
        return output