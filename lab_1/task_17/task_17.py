import time
import tracemalloc

def knight_move(n):
    moves = {
        0: [4,6],
        1: [6,8],
        2: [7,9],
        3: [4,8],
        4: [0,3,9],
        5: [],
        6: [0,1,7],
        7: [2,6],
        8: [1,3],
        9: [4,2]
    }

    if n == 1:
        return 8
    mod = 10**9
    A = []
    for _ in range(n + 1):
        p = [0] * 10
        A.append(p)


    for digit in range(8):
        A[1][digit] = 1

    for i in range(2, n + 1):
        for j in range(10):
            for move in moves[j]:
                A[i][j] = (A[i][j] + A[i - 1][move]) % mod


    return sum(A[n]) % mod

tracemalloc.start()
start_time = time.time()

with open("task_17/input.txt","r") as file:
    lines = file.readlines()

n = int(lines[0].strip())

result = knight_move(n)

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("task_17/output.txt","w") as file:
    file.write(f"Количество телефонных номеров: {str(result)}\n")
    file.write(f"Время выполнения: {execution_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")