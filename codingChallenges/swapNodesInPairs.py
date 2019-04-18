# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            head.val, head.next.val = head.next.val, head.val
            self.swapPairs(head.next.next)
        return head
