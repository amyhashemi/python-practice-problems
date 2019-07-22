
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head} #stores all nodes that we create with the next 3 lines of code
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0]) #creating nodes
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


def is_bst(node, lower_lim=None, upper_lim=None):
    if (lower_lim != None and node.value < lower_lim):
        return False
    if (upper_lim != None and node.value > upper_lim):
        return False
    
    is_left_bst = True
    is_right_bst = True

    if node.left != None:
        is_left_bst = is_bst(node.left, lower_lim, node.value)

    if (is_left_bst and node.right != None):
        is_right_bst = is_bst(node.right, node.value, upper_lim)

    return is_left_bst and is_right_bst


# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}

head1 = create_tree(mapping1, 0)
# This tree is:
#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6

head2 = create_tree(mapping2, 3)
# This tree is:
#  head2 = 3
#        /   \
#       1     4
#      /\    / \
#     0  2  5   6
head3 = create_tree(mapping3, 3)
# This tree is:
#  head3 = 3
#        /   \
#       1     5
#      /\    / \
#     0  2  4   6
head4 = create_tree(mapping4, 3)
# This tree is:
#  head4 = 3
#        /   \
#       1     5
#      /\
#     0  4

ans = is_bst(head1) #should return False
print(ans)
ans = is_bst(head2) #should return False
print(ans)
ans = is_bst(head3) #should return True
print(ans)
ans = is_bst(head4) #should return False
print(ans)