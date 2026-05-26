class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 1+d.get(i, 0)
        for k in d.keys():
            if d[k] > len(nums)/2:
                return k
        