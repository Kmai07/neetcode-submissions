class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num not in dic:
                dic[nums[i]] = i
            else:
                return [dic[num], i] 