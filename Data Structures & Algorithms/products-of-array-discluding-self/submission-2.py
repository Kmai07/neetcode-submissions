class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = []
        post = len(nums)*[]
        i = 0
        prod = 1
        pre.append(prod)
        while i<len(nums)-1:
            prod *= nums[i]
            pre.append(prod)
            i +=1
        prod2 = 1
        j = len(nums) - 1
        post.append(prod2)
        while j>= 1:
            prod2 *= nums[j]
            post.append(prod2)
            j -= 1
        post.reverse()
        for _ in range(len(nums)):
            res.append(pre[_]*post[_])
        return res


