import sys
import time
import tracemalloc

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return TreeNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            node.size = (node.left.size if node.left else 0) + 1 + (node.right.size if node.right else 0)
            return node
        self.root = _insert(self.root, key)

    def delete(self, key):
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.key = min_node.key
                node.right = _delete(node.right, min_node.key)
            node.size = (node.left.size if node.left else 0) + 1 + (node.right.size if node.right else 0)
            return node
        self.root = _delete(self.root, key)

    def key_max(self, k):
        def _key_max(node, k):
            if not node:
                return None
            right_size = node.right.size if node.right else 0
            if k <= right_size:
                return _key_max(node.right, k)
            elif k == right_size + 1:
                return node.key
            else:
                return _key_max(node.left, k - (right_size + 1))
        return _key_max(self.root, k)

sys.setrecursionlimit(10**5)

tracemalloc.start()
start_time = time.time()

bst = BST()
output = []

with open("input.txt", "r") as file:
    n = int(file.readline())
    for _ in range(n):
        comand, k = map(int, file.readline().split())
        if comand == 1 or comand == +1:
            bst.insert(k)
        elif comand == -1:
            bst.delete(k)
        elif comand == 0:
            output.append(str(bst.key_max(k)))

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("output.txt", "w") as file:
    file.write("result:\n")
    file.write("\n".join(output))
    file.write(f"\nВремя выполнения: {execution_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")