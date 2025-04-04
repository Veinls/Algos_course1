import sys
import time
import tracemalloc


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def build_tree(self, nodes_data, index=0):
        if not nodes_data or index == -1:
            return None

        key, index_left, index_right = nodes_data[index]
        node = TreeNode(key)
        node.left = self.build_tree(nodes_data, index_left)
        node.right = self.build_tree(nodes_data, index_right)
        return node

    def is_valid_bst(self, node, min_value, max_value):
        if node is None:
            return True

        if not (min_value < node.key <= max_value):
            return False

        return (self.is_valid_bst(node.left, min_value, node.key - 1) and
                self.is_valid_bst(node.right, node.key, max_value))

    def validate(self):
        if self.root is None:
            return "CORRECT"
        return "CORRECT" if self.is_valid_bst(self.root, -2 ** 31 - 1, 2 ** 31 - 1) else "INCORRECT"


tracemalloc.start()
start_time = time.time()

sys.setrecursionlimit(10 ** 5)

with open('input.txt', 'r') as file:
    data = file.readlines()

n = int(data[0].strip())
nodes = [tuple(map(int, line.split())) for line in data[1:n + 1]]

bst = BST()
bst.root = bst.build_tree(nodes)
result = bst.validate()

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("output.txt", "w") as file:
    file.write(result + "\n")
    file.write(f"Время выполнения: {execution_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")

