def validparenthesis(s:str):
    min,max=0,0
    for i in s:
        if i=='(':
            min+=1
            max+=1
        elif i==')':
             min-=1
             max-=1
        else:
           min-=1
           max+=1

        if min<0: 
            min=0
        if max<0:
            return False
    return min==0



print(validparenthesis('(**('))