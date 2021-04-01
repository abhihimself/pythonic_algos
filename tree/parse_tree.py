from stack_queue.stack_implementation import Stack
from tree.tree_using_class import Tree
import operator

def buildparsetree(exp):
    list_exp = exp.split()
    etree = Tree("")
    estack = Stack()

    estack.push(etree)
    currenttree = etree

    for item in list_exp:
        if item == "(":
            currenttree.add_left("")
            estack.push(currenttree)
            currenttree = currenttree.get_left_child()

        elif item in ['+', '-', '*', '/']:
            currenttree.set_root_value(item)
            currenttree.add_right("")
            estack.push(currenttree)
            currenttree = currenttree.get_right_child()
        elif item == ")":
            currenttree = estack.pop()
        else:
            try:
                currenttree.set_root_value(int(item))
                parent = estack.pop()
                currenttree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(item))

    return etree



def evaluate(parseTree):
    # This is post order evaluation
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.get_left_child()
    rightC = parseTree.get_right_child()

    if leftC and rightC:
        fn = opers[parseTree.get_root_value()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.get_root_value()
l = []
def inorder_evaluate(parsetree):
    # it should print the equation back
    leftC = parsetree.get_left_child()
    rightC = parsetree.get_right_child()
    if leftC:
        l.append("(")
        inorder_evaluate(leftC)
    l.append(parsetree.get_root_value())
    if rightC:
        inorder_evaluate(rightC)
        l.append(")")
pt = buildparsetree("( ( 10 + 5 ) * 3 )")
#print(evaluate(pt))

inorder_evaluate(pt)
print(l)
print("".join([str(i) for i in l]))
