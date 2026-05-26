class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = 100111
        CommonPrefix = ""
        for word in strs:
            if len(word) < min:
                min = len(word)
                shortestWord = word
        for j in range(len(shortestWord)):
            isCommon = True
            for i in strs:
                if i[j] != shortestWord[j]:
                    isCommon = False
            if isCommon:
                CommonPrefix += i[j]
            else:
                break
        return CommonPrefix


        

            