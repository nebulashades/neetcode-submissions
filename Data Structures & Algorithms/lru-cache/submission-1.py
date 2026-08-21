class Node:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.left = None
        self.right = None


class LRUCache:
    def __init__(self, capacity: int):
        self.s = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def updateList(self, key: int) -> Node:
        node = self.hashmap[key]
        node.left.right = node.right
        node.right.left = node.left

        node.right = self.tail
        node.left = self.tail.left
        self.tail.left.right = node
        self.tail.left = node
        return node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.updateList(key)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.updateList(key)
            return

        if self.s == 0:
            k = self.head.right.key
            if k in self.hashmap:
                del self.hashmap[k]
            self.head.right = self.head.right.right
            self.head.right.left = self.head
            self.s += 1

        node = Node(key=key, val=value)
        node.left = self.tail.left
        node.right = self.tail
        self.tail.left.right = node
        self.tail.left = node
        self.s -= 1
        self.hashmap[key] = node
