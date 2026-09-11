class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_of_zeros = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                product *= nums[index]
            else:
                num_of_zeros += 1
        
        result = []
        for index in range(len(nums)):
            if num_of_zeros == 1:
                if nums[index] != 0:
                    result.append(0)
                else:
                    result.append(product)
            elif num_of_zeros > 1:
                result.append(0)
            else:
                result.append(int(product / nums[index]))
        return result