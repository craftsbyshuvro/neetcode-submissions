class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, num in enumerate(nums):
            no_req = target - num

            req_num = my_dict.get(no_req)

            if req_num is not None:
                return [req_num, index]
            else:
                my_dict[num] = index
        return []

