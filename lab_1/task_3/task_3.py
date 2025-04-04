import time
import tracemalloc

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


tracemalloc.start()
start_time = time.time()

with open("task_3/input.txt", "r") as file:
    lines = file.readlines()

n = int(lines[0].strip())
a = list(map(int,lines[1].strip().split()))
b = list(map(int,lines[2].strip().split()))

bubble_sort(a)
bubble_sort(b)

max = 0
for i in range(n):
      max += abs(a[i]*b[i])

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("task_3/output.txt", "w") as file:
    file.write(f"Максимальный доход: {str(max)}\n")
    file.write(f"Время выполнения: {end_time - start_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")




