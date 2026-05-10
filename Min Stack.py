class MinStack(object):
   
    def __init__(self):
        self.st=[]
        self.minval=float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.st)==0:
            self.st.append(val)
            self.minval=val
        elif val<self.minval:
            valN=2*val-self.minval
            self.minval=val
            self.st.append(valN)
        else:
            self.st.append(val)


    def pop(self):
        """
        :rtype: None
        """
        if self.st[-1]<self.minval:
            self.minval=2*self.minval-self.st[-1]
        self.st.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.st[-1]<self.minval:
            return self.minval
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
# obj.pop()
print(obj.top())
print(obj.getMin())