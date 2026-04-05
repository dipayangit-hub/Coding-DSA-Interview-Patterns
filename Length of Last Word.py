class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        ch=s.split(" ")
        return len(ch[-1])
    
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))