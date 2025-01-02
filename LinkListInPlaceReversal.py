from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head   

# Function to display the linked list
def display_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None") 


class LinkList:          
            

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node #None is set to currentNode next
            prev_node=curr_node
            curr_node = next_node

        return prev_node                

    def reverseListBetween(self, head:Optional[ListNode], left:int, right:int)-> Optional[ListNode]:
        if not head:
            return None
        curr_node = head
        prev_node = None
        left_node = None
        right_node = None
        i =0
        j=0
        while curr_node is not None:
            if i>=left:
                if i> right:                   
                   return prev_node
                next_node = curr_node.next
                curr_node.next = prev_node #None is set to currentNode next
                prev_node=curr_node
                curr_node = next_node
                i+=1
            else:
                left_node= curr_node.val
                curr_node=curr_node.next
                i+=1

        return prev_node 

    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        for _ in range(left-1):
            prev = prev.next
        
        current = prev.next
        
        for _ in range(right - left):
                next_node = current.next
                current.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
 
            

        return dummy.next    

values = [1, 2, 3, 4, 5]
listNode = ListNode()
head = create_linked_list(values)
print(display_linked_list(head))

linkList = LinkList()
#  reverseHead=linkList.reverseList(head)
# print(display_linked_list(reverseHead))
reverseInBetween=linkList.reverseBetween(head,2,4)
print(display_linked_list(reverseInBetween))

        

