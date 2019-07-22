class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head

    
    # Implement your function below.
def lca(root, j, k):
    return None




mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
head1 = create_tree(mapping1, 0)
# This tree is:
# head1 = 0
#        / \
#       1   2
#      /\   /\
#     3  4 5  6

# lca(head1, 1, 5) should return 0
# lca(head1, 3, 1) should return 1
# lca(head1, 1, 4) should return 1
# lca(head1, 0, 5) should return 0