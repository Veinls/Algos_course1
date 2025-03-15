import time
import tracemalloc

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

# Начало отсчета времени и памяти
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
      max += a[i]*b[i]

end_time = time.time()
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
#Конец отсчета времени и памяти

with open("task_3/output.txt", "w") as file:
    file.write(f"Максимальный доход: {str(max)}\n")
    file.write(f"Время выполнения: {end_time - start_time:.6f} сек\n")
    file.write(f"Использование памяти: {memory[1] / 1024:.2f} КБ\n")




