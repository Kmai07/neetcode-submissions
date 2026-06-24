class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_a = 0
        max_len = 0
        dic = {}
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) +1
            max_a = max(dic[s[r]], max_a)
            while (r-l+1) - max_a>k:
                dic[s[l]] -= 1
                l += 1
            max_len = max(r-l+1, max_len)
        return max_len
            