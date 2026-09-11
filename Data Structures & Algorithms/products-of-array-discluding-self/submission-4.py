class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        num_contains_zero = False
        totalZero = 0
        total_product = 1

        for num in nums:
            if num != 0:
                total_product = total_product * num
            else:
                num_contains_zero = True
                totalZero = totalZero + 1

        all_num_zero = False

        if totalZero > 1:
            all_num_zero = True

        for num in nums:
            if all_num_zero is True:
                output.append(0)
            elif num == 0:
                output.append(total_product)
            else:
                if num_contains_zero is False:
                    output.append(int(total_product/num))
                else:
                    output.append(0)

        return output