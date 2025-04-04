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

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            return
        node = self.root
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = TreeNode(key)
                    return
                else:
                    node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = TreeNode(key)
                    return
                else:
                    node = node.right
            else:
                return

    def find_min_node(self, x):
        node = self.root
        result = 0
        while node is not None:
            if node.key > x:
                result = node.key
                node = node.left
            else:
                node = node.right
        return result

bst = BST()
result = []

tracemalloc.start()
start_time = time.time()

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        index = line.split()
        if index[0] == '+':
            x = int(index[1])
            bst.insert(x)
        elif index[0] == '>':
            x = int(index[1])
            res = bst.find_min_node(x)
            result.append(str(res))

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("output.txt", "w") as file:
    file.write("result:\n")
    file.write("\n".join(result))
    file.write(f"\nВремя выполнения: {execution_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")
