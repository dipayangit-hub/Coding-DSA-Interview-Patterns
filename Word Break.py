class Solution(object):
    def wordBreak(self, s, wordDict):
        #extra 1st space in aray to indicate empty string "" is possible
        dp=[False for _ in range(len(s)+1)]
        dp[0]=True #empty string is valid
        maxlen=0
        wordset=set(wordDict) #set has linear serach time
        for word in wordDict:
            maxlen=max(maxlen,len(word))
        for i in range(1,len(s)+1):
                #try forming words by conceatenating previous characters until match found but till it is within maxlen
                for j in range(i-1,max(-1,i-maxlen-1),-1):
                    word=s[j:i]
                    if dp[j] and s[j:i] in wordset:
                         dp[i]=True
                         break
        return dp[len(s)]



    
print(Solution().wordBreak("applepenapple",["apple","pen"]))