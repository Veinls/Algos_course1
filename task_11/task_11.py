import time
import tracemalloc

def knapsack(n,w,w_i):
    A =[]
    for _ in range(n + 1):
        p = [0] * (w + 1)
        A.append(p)
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                A[i][j] = 0
            elif w_i[i - 1] <= j:
                A[i][j] = max(A[i - 1][j],A[i - 1][j - w_i[i - 1]]+w_i[i - 1])
            else:
                A[i][j] = A[i - 1][j]

    return A[n][w]


tracemalloc.start()
start_time = time.time()

with open("task_11/input.txt","r") as file:
    lines = file.readlines()

w = int(lines[0].strip().split()[0])
n = int(lines[0].strip().split()[1])
w_i = list(map(int,lines[1].strip().split()))

max_value = knapsack(n, w, w_i)

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("task_11/output.txt","w") as file:
    file.write(f"Максимальный вес золота: {max_value}\n")
    file.write(f"Время выполнения: {execution_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")