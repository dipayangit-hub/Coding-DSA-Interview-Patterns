class StockSpanner:

    def __init__(self):
        self.st=[]
        self.spans=[]
        self.arr=[]

    def next(self, price: int) -> int:
        self.arr.append(price)
        index=len(self.arr)-1
       
        while len(self.st)>0 and self.arr[self.st[-1]]<=price:
            self.st.pop()
        span=index-self.st[-1] if len(self.st)>0 else index+1
        self.spans.append(span)
        self.st.append(index)
        return self.spans[-1]
               


stockSpanner=StockSpanner()
stockSpanner.next(31)
stockSpanner.next(41)
stockSpanner.next(48)
stockSpanner.next(59)
stockSpanner.next(79)
# stockSpanner.next(75)
# stockSpanner.next(85)