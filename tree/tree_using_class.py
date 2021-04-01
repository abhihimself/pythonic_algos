class Tree:
    def __init__(self, root_val):
        self.root = root_val
        self.left = None
        self.right = None

    def add_left(self, left_val):
        new_node = Tree(left_val)
        if not self.left:
            self.left = new_node
        else:
            new_node.left = self.left
            self.left = new_node

    def add_right(self, right_val):
        new_node = Tree(right_val)
        if not self.right:
            self.right = new_node
        else:
            new_node.right = self.right
            self.right = new_node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_root_value(self):
        return self.root

    def set_root_value(self, root_value):
        self.root = root_value

if __name__ == '__main__':

    t = Tree(2)
    t.add_left(3)
    t.add_right(4)

    print(t.get_root_value())
    print(t.get_left_child().root)