def jobsequencing(id:list,deadline:list,proft:list):
    res=[-1]*(len(id)-1)
    count,tf=0,0
    for i in range(0,len(id)):
        j=deadline[i]
        while j>=0:
            if res[j]==-1:
                count+=1
                tf+=proft[i]
                res[j]=id[i]
                break
            j-=1
    return count,tf   



        





print(jobsequencing([6,3,4,2,5,8,1,7],[2,6,6,5,4,2,4,2],[80,70,65,60,25,22,20,10]))