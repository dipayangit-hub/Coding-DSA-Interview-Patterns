class Solution(object):
    def longestCommonPrefix(self, strs):
        #sorting groups words
        strs.sort()
        pref=""
        i=0
        #the first and extreme last word will have the max difference when array is sorted or strings are grouped together
        word=strs[0]
        word1=strs[len(strs)-1] 
        #word will have the minimum length
        while i<len(word):
            if word[i]!=word1[i]:
                break
            pref+=word[i]
            i+=1
        return pref


    
print(Solution().longestCommonPrefix(["flower","flow","flight"]))

