# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head or head.next is pointing to null, then return the current head
        if not head or not head.next : 
            return head
        
        left = head # assign the starting head pos to left pointer
        right = self.getMid(head) # the getmid() return the exact mid node of a given list from 'head'
        tmp = right.next # storing the next node of right temporary
        right.next = None # assigning null to next node of right to virtually split the list into 2 parts
        right = tmp # re-attach the right node to right pointer

        left = self.sortList(left) # recursively calls the primary 'sortList()' to seperate the nodes of the left list into individual nodes
        right = self.sortList(right) # recursively calls the primary 'sortList()' to seperate the nodes of the right list into individual nodes
        return self.mergeList(left,right) # recursively merges the nodes in assending order until null isn't reached
    
    def getMid(self,head) : 
        # utilizing 2 pointer technique to split a list into 2 seperate parts, where fast pointers jumps by 2 & slow pointer jumps by 1, thereby when fast pointer is pointing to null at the same time the slow pointer will exactly be pointing to the mid node of the list
        slow, fast = head, head.next
        while fast and fast.next : 
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeList(self,left,right) :
        # asically dummy and tail are two different POINTER nodes starting at the same spot of the Linked List we created. It is more accurate to understand them as POINTER instead of nodes. 
        
        # In the code we do dummy= tail= Node(), that means we created 2 different pointers starting at the same Linked List Node.  Then going forward dummy node stays at the starting points, but tail pointer keeps moving forward, which is to add new nodes to the LinkedList we created. 
        tail = dummy = ListNode() 
        while left and right : # while nodes in left & right persist
            if left.val < right.val : # if left node's value is less than the node in right list then attach the left node to tail else attach the right node to tail
                tail.next = left
                left = left.next
            else : 
                tail.next = right
                right = right.next
            tail = tail.next # move the tail pointer forward to add more nodes
        
        if left : # if there are sorted nodes in the left/right list then attach them to tail position
            tail.next = left
        if right : 
            tail.next = right
        
        return dummy.next # by returning dummy's next node, we are essentially returning the whole sorted list
# Time Complexity: O(n log n), where n is the number of nodes in the linked list.
# Space Complexity: O(log n), due to the recursive call stack.