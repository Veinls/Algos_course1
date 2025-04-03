import time
import tracemalloc
import random

def quicksort(arr, left, right):
    if left >= right:
        return
    i, j =  left, right
    pivot = arr[random.randint(left,right)][1]
    while i <= j:
        while arr[i][1] < pivot:
            i += 1
        while arr[j][1] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    quicksort(arr, left, j)
    quicksort(arr, i, right)

tracemalloc.start()
start_time = time.time()

with open("task_4/input.txt","r") as file:
    lines = file.readlines()

n = int(lines[0].strip())
segment_list = []
for s in range(1, n+1):
    a,b = list(map(int,lines[s].strip().split()))
    segment_list.append((a, b))

quicksort(segment_list, 0, len(segment_list) - 1)

point = []
last_point = -1

for segment in segment_list:
    a, b = segment
    if last_point < a:
        last_point = b
        point.append(last_point)

points = len(point)
coordinates_points = " ".join(map(str, point))

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("task_4/output.txt", "w") as file:
    file.write(f"Количество точек: {points}\n")
    file.write(f"Координаты точек: {coordinates_points}\n")
    file.write(f"Время выполнения: {execution_time:.6f} сек\n")
    file.write(f"Использование памяти (текущая): {current / 1024:.6f} КБ\n")
    file.write(f"Использование памяти (пик): {peak / 1024:.6f} КБ\n")