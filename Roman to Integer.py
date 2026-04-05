class Solution(object):
    def romanToInt(self, s):
        map={}
        map['I']=1
        map['V']=5
        map['X']=10
        map['L']=50
        map['C']=100
        map['D']=500
        map['M']=1000

        res,i=0,0
        while i<len(s)-1:
            if map[s[i]]<map[s[i+1]]:
                res-=map[s[i]]
            else:
                res+=map[s[i]]
            i+=1
        
        return res+map[s[i]]
    
print(Solution().romanToInt("MCMXCIV"))