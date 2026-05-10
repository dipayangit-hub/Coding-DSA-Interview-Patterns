class Solution(object):
    def spiralOrder(self, matrix):
        m=len(matrix)
        n=len(matrix[0])

        top,bot=0,m-1
        l,r=0,n-1
        res=[]
        while l<=r and top<=bot:
            #left -> right
            for i in range(l,r+1):
                res.append(matrix[top][i])
            top+=1
            #top+1->bottom
            for i in range(top,bot+1): 
                res.append(matrix[i][r])
            r-=1
            #right->left (ignore if no other row is left to be traversed) - for handling just 1 row
            if top<=bot:
                for i in range(r,l-1,-1):
                    res.append(matrix[bot][i])
                bot-=1
            #bottom->top (ignore if no other column is left to be traversed) - for handling just 1 column
            if l<=r:
                for i in range(bot, top-1,-1):
                    res.append(matrix[i][l])
            l+=1

        return res
    

print(Solution().spiralOrder([[7],[9],[6]]))


            

            
            

        

                
