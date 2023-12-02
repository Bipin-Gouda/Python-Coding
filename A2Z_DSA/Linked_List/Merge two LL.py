'''
Merge Two Sorted Linked List
You are given the heads of two sorted linked lists list1 and list2. 
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.   

Example 1: 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3: 
Input: list1 = [], list2 = [0]
Output: [0]'''


# Note the code will not run as there is no insertion and all but we can refer the code.
#%%
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):

        # SOLUTION 1 (BEST SOLUTION AND SIMPLE)

        prehead = ListNode(-1)          #Dummy node to make things easier
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
        return prehead.next
    

#%%

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t1=l1
        t2=l2
        t3=None
        if l1==None:
            return t2
        elif l2==None:
            return t1
        else:
            while(t1!=None and t2!=None):
                if t1.val<=t2.val:
                    if t3==None:
                        t3=ListNode(t1.val)
                        head=t3
                        curr=t3
                        t1=t1.next
                    else:
                        t4=ListNode(t1.val)
                        curr.next=t4
                        curr=t4
                        t1=t1.next
                else:
                    if t3==None:
                        t3=ListNode(t2.val)
                        head=t3
                        curr=t3
                        t2=t2.next
                    else:
                        t4=ListNode(t2.val)
                        curr.next=t4
                        curr=t4
                        t2=t2.next
            curr.next = t1 if t2 is not None else t2
                    
            return head