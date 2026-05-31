class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = []
        for i, t in enumerate(temperatures):
            while len(st)>0 and t>temperatures[st[-1]]:
                t_ind = st.pop()
                res[t_ind] = i - t_ind
            st.append(i)
        return res
