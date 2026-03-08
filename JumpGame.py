def jumpGame(arr:list):
    maxin=0
    for i in range(len(arr)):
        if i>maxin:
            return False
        maxin=max(maxin,i+arr[i])
        if maxin>=len(arr)-1:
            return True
    return True

        





print(jumpGame([1,2,4,1,1,0,2,5]))