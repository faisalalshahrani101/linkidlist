class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval= None
    def listprint(self):
        printval= self.headval
        while printval is not None:
            print(printval.dataval)
            printval= printval.nextval
list= SLinkedList()
list.headval = Node("faisal")
l2= Node("abdullah")
l3= Node("alsharani")
list.headval.nextval = l2
l2.nextval= l3
list.listprint()
        
