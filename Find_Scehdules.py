def find_schedules(pattern, target_hours, max_per_day):
    sum=0
    pos=[]

    for i in range(len(pattern)):
        if pattern[i]=='?':
            pos.append(i)
        else:
            sum+= int(pattern[i])
    
    remaining=target_hours-sum

    if remaining<0 or remaining>len(pos)*max_per_day:
        return []
    
    result=[]

    def replace_string(l):
        nonlocal pattern
        ch=list(pattern)
        for i in range(len(l)):
            ch[pos[i]]=str(l[i])
        result.append("".join(ch))


    def backtrack(index, sum, l):
        if index==len(pos):
            if sum==remaining:
                replace_string(l)
            return

        for hours in range(max_per_day+1):
            if hours+sum<=remaining:
                 l.append(hours)
                 backtrack(index+1,sum+hours,l)
                 l.pop()
    
    backtrack(0,0,[])
    return result


print(find_schedules("8??8967",43,4))