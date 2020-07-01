class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.val)
            printval = printval.next

    def middle(self,item):
        first = item.headval
        secont = item.headval
        result = []

        while first is not None:

            result.append(first.val)
            first = first.next.next

            secont = secont.next
        return secont
    


    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode
        return

    
       
    
def mergeTwoLists(l1, l2):
        temp = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            temp = l1
            temp.next = mergeTwoLists(l1.next,l2)
        else:
            temp = l2
            temp.next = mergeTwoLists(l1,l2.next)
        return temp

l1 = SLinkedList()
l1.headval = Node(1)

l2 =  Node(2)
l3 =  Node(3)
l5 =  Node(4)
l6 =  Node(5)
l12 =  Node(7)
l1.headval.next = l2
l2.next = l3
l3.next = l5
l5.next = l6
l6.next = l12
l4 = SLinkedList()
l4.headval = Node(1)
l5 =  Node(4)
l6 =  Node(5)
l4.headval.next = l5
l5.next = l6
l11 = SLinkedList()
l11.headval = Node(2)
l12 =  Node(7)
l13 =  Node(10)
l11.headval.next = l12
l12.next = l13
l10 = SLinkedList()
print(l10.middle(l1))

#l10.headval = mergeTwoLists(l1.headval,l4.headval)
#l10.listprint()

# lists = [l1,l4,l11]
# for x in lists:
# 	l10.headval = mergeTwoLists(l10.headval,x.headval)
#
# l10.listprint()
	
