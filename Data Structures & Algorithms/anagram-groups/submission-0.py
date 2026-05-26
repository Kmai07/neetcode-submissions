class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in ans:
                ans[k] = [i]
            else:
                ans[k].append(i)
        return list(ans.values())
            
