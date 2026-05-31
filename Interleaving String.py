class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if len1+len2!=len3:
            return False
        
        dp=[False for _ in range(len2+1) ]
        dp[0]=True

        for j in range(1, len2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]


        for i in range(1, len1 + 1):

            # First column (using only s1)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, len2 + 1):

                dp[j] = (
                    dp[j] and s1[i - 1] == s3[i + j - 1]
                ) or (
                    dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[len2]
        


print(Solution().isInterleave( s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))


        
