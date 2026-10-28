# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        store=[]
        for l in lists:
            while l:
                store.append(l.val)
                l=l.next
        store.sort()
        res=cur=ListNode()
        for n in store:
            cur.next=ListNode(n)
            cur=cur.next
        return res.next