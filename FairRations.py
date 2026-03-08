def fairRations(B):
    breads=0
    for i in range(len(B)-1):
        if B[i]%2==1:
            breads+=2
            B[i]+=1
            B[i+1]+=1
    if B[len(B)-1]%2==1:
        return 'NO'
    return str(breads)
    

if __name__ == "__main__":
    print(fairRations([4,5,6,7]))
