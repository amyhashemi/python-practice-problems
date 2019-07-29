# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        #initialize a new node to start building our linked list with
        node = ListNode(None)
        overflow = 0
        length = len(l1)

        while (l1 != None) and (l2 != None):
            for i in range(0, length):
                if (l1[i] + l2[i] > 9):
                    overflow = (l1[i] + l2[i]) % 10
                    node.val = int(str(overflow)[:1])   #only add in the first digit of the string                    
                    newNode = ListNode(overflow)
                    newNode = node.next

                else:
                    node.val = l1[i] + l2[i]
                    newNode = ListNode(None)
                    newNode = node.next


        while node.next != None:
            return node


result = Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])

print(result)


