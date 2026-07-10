class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_no_zero = 1
        zero_count = 0
        for i in range(len(nums)):
            if(nums[i])== 0:
                zero_count += 1
            else:
                product_no_zero = product_no_zero * nums[i]
        output = []
        for j in range(len(nums)):
            if nums[j] == 0:
                if zero_count>1:
                    output.append(0)
                else:
                    output.append(product_no_zero)
            else:
                if zero_count>0:
                    output.append(0)
                else:
                    output.append(int(product_no_zero/nums[j]))
        return output
