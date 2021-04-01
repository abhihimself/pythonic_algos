def init_binary_tree(root_value):
    # root with left subtree and right subtree
    return [root_value, [], []]


def insert_left(tree, value):
    l = len(tree)
    if l > 1:
        t = tree.pop(1)
        tree.insert(1, [value, t, []])
    else:
        tree.insert(1, [value, [], []])
    return tree


def insert_right(tree, value):
    l = len(tree)
    if l > 1:
        t = tree.pop(2)
        tree.insert(2, [value, [], t])
    else:
        tree.insert(2, [value, [], []])
    return tree

my_tree = init_binary_tree(1)
my_tree = insert_left(my_tree, 1)
print(my_tree)