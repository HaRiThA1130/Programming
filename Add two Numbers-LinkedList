** class Solution: **
**    def addTwoNumbers(self, l1, l2):**
**        h = ListNode(0)**
**        t = h**
**        c = 0**

**        while l1 or l2 or c:**
**            if l1:**
**                c += l1.val**
**                l1 = l1.next**
**            if l2:**
**                c += l2.val**
**                l2 = l2.next**

**            t.next = ListNode(c % 10)**
**            t = t.next**
**            c //= 10**

**        return h.next**




# Definition for singly-linked list.
# A ListNode stores:
# 1) a digit (val)
# 2) the address of the next node (next)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to start the result linked list
        # This helps us easily return the final list
        h = ListNode(0)

        # 'n' is used to move through the result list
        n = h

        # 'c' stores the carry value (like carry in normal addition)
        c = 0

        # Loop runs while there is a node in l1, l2, or carry is left
        while l1 or l2 or c:

            # If l1 exists, add its value to carry
            if l1:
                c = c + l1.val
                l1 = l1.next   # move to next node of l1

            # If l2 exists, add its value to carry
            if l2:
                c = c + l2.val
                l2 = l2.next   # move to next node of l2

            # Create a new node with last digit of sum
            # Example: if c = 12, store 2
            n.next = ListNode(c % 10)

            # Move to the next node in result list
            n = n.next

            # Update carry (example: 12 → carry becomes 1)
            c = c // 10

        # Return the result linked list (skip dummy node)
        return h.next
