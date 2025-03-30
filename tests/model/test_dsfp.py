from model.dfsp import dsfp

class DummyNode:

    def __init__(self,value):
        self.value = value
        self.children = list()

    def __sub__(self, other):
        self.children.append(other)
        return other

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

fn_children = lambda node: node.children
fn_aggregate = lambda node : print(f"aggregated: {node=}")
fn_leaf = lambda node : print(f"leaf applied: {node=}")

allow_loops = True
reverse_children = True

args = (fn_children, fn_aggregate, fn_leaf, allow_loops, reverse_children)


root = DummyNode("root")
a = DummyNode("a")
b = DummyNode("b")
c = DummyNode("c")
b1 = DummyNode("b1")
b2 = DummyNode("b2")
c1 = DummyNode("c1")
bc1 = DummyNode("bc1")
loop = DummyNode("loop")

root - a
root - c -c1 - bc1
root - b - b1 -bc1
b-b2
b1-loop-root

#loop-root

dsfp(root, *args)