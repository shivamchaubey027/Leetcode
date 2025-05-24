# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode();
        tail=dummy;
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next    
            tail=tail.next

        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        
                            
        return dummy.next


##Here we just do the same m+n solution we check the heads of it and go on to merge the listNode behind the ListNode which is smaller, Accha we can do recurssion thing too but we avoid it here

##Okay I did write the recursionb wala solution, It wasnt  very difficult, Do we really need no loops in recursion , Woahh
##Also I did get stuckinlist1.val which outputs only the value but we had to return the whole list1, object
 if not list1:
            return list2
        if not list2:
            return list1

        if(list1.val< list2.val):
            list1.next= self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next= self.mergeTwoLists(list1, list2.next)
            return list2

