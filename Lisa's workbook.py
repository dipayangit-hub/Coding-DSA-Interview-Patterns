def workbook(n,k,arr):
    count=0
    page=1

    for probs in arr:
        for prob in range(1,probs+1):
            if prob==page:
                count+=1
            if prob%k==0 or prob==probs:
                page+=1
    return count
            


def main():
    print(workbook(5,3,[4,2,6,1,10]))

main()