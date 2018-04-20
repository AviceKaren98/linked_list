
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SingleLinkedList:
    def __init__(self):
       self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
       self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr
    
    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
            
    def addEnd(self, data):
        if self.head is None:
            self.head=data
        else:
            temp=self.head
            while(temp.next != None):
                temp=temp.next
            temp.next=data
            
    def detectCycle(self):
        fastptr=self.head
        slowptr=self.head
        
        while(fastptr != None and fastptr.next != None):
            fastptr=fastptr.next
            fastptr.next=fastptr.next
            slowptr=slowptr.next
            if(slowptr == fastptr):
                return 1
        return 0
    
               
    def getCount(self):
        temp = self.head 
        count = 0  
        while (temp):
            count += 1
            temp = temp.next
        return count

    def printList(self):
        temp=self.head
        while(temp):
            print (temp.data)
            temp=temp.next

                  
if __name__=='__main__':
    node = SingleLinkedList()
    node.append(1)
    node.append(2)
    node.append(3)
    node.append(4)
    node.append(5)
    node.append(6)
    print("new list after append \t")
    node.printList()
    print("number of nodes",node.getCount())
    node.prepend(0)
    print("new list after prepend \t")
    node.printList()
    print("number of nodes",node.getCount())
    node.addEnd(4)
    print("cycle is true(1) or false(0):",node.detectCycle())
    
            
        
    
    
