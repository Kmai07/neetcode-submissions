class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in has:
                return [has[difference],i]
            else:
                has[nums[i]] = i
         