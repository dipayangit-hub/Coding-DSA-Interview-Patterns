import random
class RandomizedSet:

    def __init__(self):
        self.arr=[] #to maintain indexes as set doesnt support indexing
        self.map={} #O(1) time complexity of seraching

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        #add length of arr= current index to dict
        self.map[val]=len(self.arr)
        self.arr.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        pos=self.map[val]
        last = self.arr[-1]
        # move last element to pos and update the dict pos for last value that was moved
        self.arr[pos] = last
        self.map[last]=pos
        #remove last and remove from dict
        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())
print(obj.getRandom())
# print(obj.remove(1))
# print(obj.insert(2))