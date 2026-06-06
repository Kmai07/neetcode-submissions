class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_ar = 0
        while i<j:
            if heights[j]>=heights[i]:
                ar = heights[i]*(abs(j-i))
                if ar>max_ar:
                    max_ar = ar
                i+=1
            else:
                ar = heights[j]*abs(j-i)
                if ar>max_ar:
                    max_ar = ar
                j -= 1
        return max_ar
