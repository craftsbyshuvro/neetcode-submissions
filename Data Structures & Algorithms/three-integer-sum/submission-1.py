class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        result = []
        for index in range(len(nums)):

            if index > 0 and nums[index] == nums[index-1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                all_sum = nums[index] + nums[left] + nums[right]
                if all_sum < target:
                    left +=1
                elif all_sum > target:
                    right -=1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left +=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    
                    right -=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
        return result

