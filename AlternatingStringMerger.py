class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        list=[ word1,word2]
        list=sorted(list,key=len)
        smallerWord= list[0]
        biggerWord=list[1]
        for i in range (len(smallerWord)):
            result+=word1[i]
            result+=word2[i]
        result+=biggerWord[len(smallerWord):]
        return result
        