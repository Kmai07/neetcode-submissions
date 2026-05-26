class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        d = {}
        for j in range(len(nums)):
            difference = target - nums[j]
            if difference in d:
                return [d[difference], j]
            else:
                d[nums[j]] = j

            
