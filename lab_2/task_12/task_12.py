import sys
import time
import tracemalloc

class TreeBalancer:
    def __init__(self, n):
        self.n = n
        self.left_child = [0] * (n + 1)
        self.right_child = [0] * (n + 1)
        self.height = [0] * (n + 1)
        self.balance = [0] * (n + 1)

    def build_tree(self, nodes):
        for i in range(1, self.n + 1):
            _, left, right = nodes[i - 1]
            self.left_child[i] = left
            self.right_child[i] = right

    def compute_height(self, node_num):
        if node_num == 0:
            return 0
        if self.height[node_num] != 0:
            return self.height[node_num]

        left_h = self.compute_height(self.left_child[node_num])
        right_h = self.compute_height(self.right_child[node_num])

        self.height[node_num] = 1 + max(left_h, right_h)
        self.balance[node_num] = right_h - left_h

        return self.height[node_num]

    def compute_balances(self):
        for i in range(1, self.n + 1):
            self.compute_height(i)
        return self.balance[1:self.n + 1]


sys.setrecursionlimit(10**5)
tracemalloc.start()
start_time = time.time()

with open('input.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())
nodes = []
for line in lines[1:n + 1]:
    parts = list(map(int, line.strip().split()))
    nodes.append(parts)

balancer = TreeBalancer(n)
balancer.build_tree(nodes)
balances = balancer.compute_balances()

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open('output.txt', 'w') as file:
    for balance in balances:
        file.write(f"{balance}\n")
    file.write(f"Время выполнения: {execution_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")
