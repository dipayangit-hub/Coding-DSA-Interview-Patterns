class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        l,r=0,len(s1)-1
        freq1=[0]*26
        freq2=[0]*26
        #first check the initial window and return true if matching
        for i in range(len(s1)):
            freq1[ord(s1[i])-ord('a')]+=1
            freq2[ord(s2[i])-ord('a')]+=1
        
        if freq1==freq2:
            return True
        l=0
        #start r after initial window, i.e. 2 in this case
        for r in range(len(s1),len(s2)):
            #add new on right and remove left to maintain window of size(s1)
            freq2[ord(s2[r])-ord('a')]+=1
            freq2[ord(s2[l])-ord('a')]-=1    
            if freq1==freq2:
                return True 
            l+=1
  
        return False



        


print(Solution().checkInclusion("ab","eidbaooo"))