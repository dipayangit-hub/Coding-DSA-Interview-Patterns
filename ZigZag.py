class Solution(object):
    def convert(self, s, numRows):
        i=0
        row=["" for _ in range(numRows)]
        while i<len(s):
            r=0
            #going down
            while r<numRows and i<len(s): 
                row[r]+=s[i]
                r+=1
                i+=1
                
            #coming up
            r=numRows-2
            while r>0 and i<len(s):
                row[r]+=s[i]
                r-=1
                i+=1
         
        return "".join(row)
    

print(Solution().convert("PAYPALISHIRING",3))