class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic ={}
        for i in range(len(s)):
            if s[i] not in dic:
                l = list(dic.values())
                dic[s[i]] = t[i]
                if dic[s[i]] in l:
                    return False
            else:

                if dic[s[i]] != t[i]:
                    return False
                
        return True
            
