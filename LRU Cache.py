class DoubleLinkedlist:
    def __init__(self, val=0, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.capacity = capacity
        self.map = {}

        self.head = DoubleLinkedlist([-1, -1])
        self.tail = DoubleLinkedlist([-1, -1])

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node):
        prev_node,next_node=node.prev,node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def appendatstart(self,node):
        curr=self.head.next
        curr.prev,self.head.next=node,node
        node.next=curr
        node.prev=self.head

    def get(self, key: int) -> int:
         if key in self.map:
            node=self.map[key]
            value=node.val[1]
            self.remove(node)

            #creation of new node at start
            self.appendatstart(node)
            self.map[key]=node
            return value
         return -1

    def put(self, key: int, value: int) -> None:

        if key in self.map:
            old_node=self.map[key]
            self.remove(old_node)

        elif len(self.map)==self.capacity:
            old_node=self.tail.prev
            oldkey=old_node.val[0]
            
            self.remove(old_node)
            self.map.pop(oldkey)

      

        #creation of updated node
        node=DoubleLinkedlist([key,value])
        self.appendatstart(node)
        self.map[key]=node
       
            

obj=LRUCache(4)
obj.put(2,6)
obj.put(4,7)
obj.put(8,11)
obj.put(7,10)

print(obj.get(2))
print(obj.get(8))
obj.put(5,6)
print(obj.get(7))

obj.put(5,7)



