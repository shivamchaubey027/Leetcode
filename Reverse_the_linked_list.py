# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        curr=head
        nextNode= None
        while(curr!=None):
            nextNode= curr.next
            curr.next= prev
            prev=curr
            curr=nextNode
        
        return prev
             
            
##Okay so this is mostly the same for everytime Our basic aim here is first to point the current node to some dummy empty 'prev'node. But if we do this directly, the next node in the linked list will get delinked and disappear.

###So before linking the current node to the previous one, what we do is store the next node in a variable called nextNode. Then we set current.next to prev.

###Now we have reversed the link for the current node. To move forward, we make prev equal to current, and current equal to nextNode.

###This is a very classic approach
        
