
class Node:

    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def nth_from_last(self, head, n):

        first_head = head
        second_head = head

        if head is None:
            return None

        for i in range(0, n):
            if second_head == None:
                return None
            second_head = second_head.child

        while second_head is not None:
            first_head = first_head.child
            second_head = second_head.child

        element = first_head.value
        
        return element



current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2
# head2 = 1 -> 2 -> 3 -> 4 -> (None)

# element = head.nth_from_last(head, 1)
# print(element)

element = head.nth_from_last(head, 1) #should return 1.
print(element)
element = head.nth_from_last(head, 5) #should return 5.
print(element)
element = head.nth_from_last(head2, 2) #should return 3.
print(element)
element = head.nth_from_last(head2, 4) #should return 1.
print(element)
element = head.nth_from_last(head2, 5) #should return None.
print(element)
element = head.nth_from_last(None, 1) #should return None.
print(element)