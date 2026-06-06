class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                if ord(i)>=65 and ord(i)<=90:
                    new_s += chr(ord(i) + 32)
                else:
                    new_s += i
        i = 0
        j = len(new_s)-1
        flag = True
        while i<j:
            flag = False
            if new_s[i] != new_s[j]:
                i += 1
                j -= 1
                return flag
            if new_s[i] == new_s[j]:
                i += 1
                j-= 1
                flag = True
        return flag