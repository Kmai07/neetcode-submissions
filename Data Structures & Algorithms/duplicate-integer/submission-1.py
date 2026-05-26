class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDub = False
        lst = {}
        for i in range(len(nums)):
            if nums[i] not in lst:
                lst[nums[i]] = 1
            else:
                lst[nums[i]] += 1
        k = list(lst.values())
        for j in k:
            if j>1:
                isDub = True
        return isDub
            
