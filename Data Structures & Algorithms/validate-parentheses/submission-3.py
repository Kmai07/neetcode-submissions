class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if (i=="[") or (i=="{") or (i=="("):
                res.append(i)
            else:
                if len(res) > 0:
                    if (i=="]" and res[-1]=="[") or (i==")" and res[-1]=="(") or (i=="}" and res[-1]=="{"):
                        res.pop()
                    else:
                        res.append(i)
                else:
                    res.append(i)
                
        if len(res) == 0:
            return True
        else:
            return False
