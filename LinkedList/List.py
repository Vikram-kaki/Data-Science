


class List:
    
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.next = None
            
    
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        
    def addElementsStart(self,value):
        if self.head == None:
            self.head = self.Node(value)
            
        else:
            temp = List.Node(value)
            temp.next = self.head  # type: ignore
            self.head = temp
            
        self.length += 1
    
    def getHeadValue(self):
        if self.head != None:
            return self.head.value
        
    def addElementAtEnd(self, value):
        if self.head == None:
            self.head = self.Node(value)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
                
            temp.next = self.Node(value) # type: ignore
        self.length += 1
        
        
        
    def removeElement(self,value):
        
        if self.head == None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            return True
        
        temp = self.head
        temp2 = None
        found = False
        while temp.next != None:
            temp2  = temp
            temp = temp.next
            if temp.value == value:
                found = True
                break
            
        if found:
            temp2.next = temp.next # type: ignore
            return True
        return False

    
    def reverse(self):
        if self.head == None:
            return False
        
        
        prev = None
        curr = self.head
        
        while curr != None:
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next
            
        self.head = prev
        
        
        
        
            
    
    def printElements(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
            
            
            
list = List()
list.addElementsStart(2)
list.addElementsStart(4)
list.addElementAtEnd(5)
print(list.getHeadValue())
list.printElements()

print(list.removeElement(4))
list.printElements()
print(list.removeElement(5))
list.printElements()

list.addElementsStart(2)
list.addElementsStart(4)
list.addElementAtEnd(5)

list.printElements()

list.reverse()

list.printElements()
