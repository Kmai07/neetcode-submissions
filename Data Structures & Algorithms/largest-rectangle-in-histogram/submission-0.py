class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = []
        heights.append(0)
        for w, h in enumerate(heights):
            start = w
            while len(st)>0 and h<st[-1][1]:
                pop_w, pop_h = st.pop()
                ar = (w-pop_w)*pop_h
                if ar>res:
                    res = ar
                start = pop_w
            st.append((start, h))
        return res