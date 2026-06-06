class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])
        max_right = [0]*(len(height))
        max_right[len(height)-1] = height[len(height)-1]
        j = len(height)-2
        while j>=0:
            max_right[j] = max(max_right[j+1], height[j])
            j -= 1
        trap_water = 0
        for i in range(len(height)):
            if max_right[i]>height[i] and max_left[i]>height[i]:
                trap_water += min(max_left[i], max_right[i]) - height[i]
        return trap_water