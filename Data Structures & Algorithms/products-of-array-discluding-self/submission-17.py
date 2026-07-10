class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        prefix = 1
        for i in range(1, len(nums)):
            prefix = prefix*nums[i-1]
            prefix_products.append(prefix)
        suffix_products = [1]
        suffix  = 1
        for i in range(len(nums)-1, 0, -1):
            suffix = suffix*nums[i]
            suffix_products.append(suffix)
        suffix_products.reverse()
        output = []
        for i in range(len(nums)):
            output.append(suffix_products[i]*prefix_products[i])
        return output