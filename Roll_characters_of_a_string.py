def rollcharacters(s:str,roll:list):
    chars=list(s)
    diff=[0 for i in range(len(s)+1)]

    for i in range(len(roll)):
        diff[0]+=1
        diff[roll[i]]-=1

    for i in range(1, len(diff)):
        diff[i] += diff[i-1]

    for i in range(len(s)):
        for j in range(diff[i]):
            if chars[i] == 'z':
                chars[i] = 'a'
            elif chars[i] == 'Z':
                chars[i] = 'A'
            else:
                chars[i] = chr(ord(chars[i]) + 1)    
             
    return "".join(chars)     
                 
    




def main():
    print(rollcharacters('bca',[1,2,3]))
main()