class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        for index in range(len(nums)):
            if index == 0:
                left.append(nums[index])
            else:
                left.append(left[index - 1] * nums[index])

        right = [1] * len(nums)
        for index in reversed(range(len(nums))):
            if index == len(nums) - 1:
                right[index] = nums[index]
            else:
                right[index] = (right[index + 1] * nums[index])

        result = []
        for index in range(len(nums)):
            if index == 0:
                result.append(right[index+1])
            elif index == len(nums) - 1:
                result.append(left[index-1])
            else:
                result.append(left[index-1] * right[index+1])
        return result