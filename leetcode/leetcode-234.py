# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        lst = []
        temp = head
        while(temp):
            lst.append(temp.val)
            temp = temp.next
        if (lst == lst[::-1]):
            return True
        else:
            return False
