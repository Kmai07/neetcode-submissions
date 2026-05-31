class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        st = []
        for pos, spd in cars:
            time = (target-pos)/spd
            st.append(time)
            while len(st)>1 and st[-1]<=st[-2]:
                st.pop()
        return len(st)
