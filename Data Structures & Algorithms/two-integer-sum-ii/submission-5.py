class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers)):
            left = 0
            right = len(numbers) - 1
            diff = target - numbers[index]

            while left <= right:
                mid = int((left + right) / 2)
                if numbers[mid] < diff:
                    left = mid + 1
                elif numbers[mid] > diff:
                    right = mid - 1
                else:
                    if index != mid:
                        return [index+1, mid+1]
                    elif mid < right:
                        left = mid + 1
                    else:
                        right = mid - 1

        return []