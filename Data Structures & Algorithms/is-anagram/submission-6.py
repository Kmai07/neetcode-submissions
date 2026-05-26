class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isAna = True
        if len(s) == len(t):
            dict_s = {}
            dict_t = {}
            for i in s:
                if i not in dict_s:
                    dict_s[i] = 1
                else:
                    dict_s[i] += 1
            for j in t:
                if j not in dict_t:
                    dict_t[j] = 1
                else:
                    dict_t[j] += 1
            for k in dict_s.keys():
                if k in dict_t:
                    if dict_s != dict_t:
                        isAna = False
                else:
                    isAna = False
        else:
            isAna = False
        return isAna
            
        
        