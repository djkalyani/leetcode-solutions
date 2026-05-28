# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''def reverse(head):
        prev,next = None,None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        second = reverse(slow)
        first = head
        while second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]


