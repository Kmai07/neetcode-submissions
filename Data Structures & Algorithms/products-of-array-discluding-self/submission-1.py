class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prod = 1
            j = 0
            while j<len(nums):
                if j != i:
                    prod *= nums[j]
                j += 1
            res.append(prod)
        return res