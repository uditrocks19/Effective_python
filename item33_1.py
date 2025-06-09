# binary tree indexing semantics

class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class IndexableTree(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield  from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f"index {index} is out of range")

    def __iter__(self):
        for node in self._traverse():
            yield node.value

obj = IndexableTree(
    10,
    left=IndexableTree(5, right=IndexableTree(9)),
    right=IndexableTree(13)
)

print(list(obj))
print(obj[2])

