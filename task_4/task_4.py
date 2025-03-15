import time
import tracemalloc

with open("task_4/input.txt","r") as file:
    lines = file.readlines()

tracemalloc.start()
start_time = time.time()

n = int(lines[0].strip())
segment_list = []
for s in range(1, n+1):
    a,b = list(map(int,lines[s].strip().split()))
    segment_list.append((a, b))

segment_list.sort(key = lambda x: x[1])
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
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

with open("task_4/output.txt", "w") as file:
    file.write(f"Количество точек: {points}\n")
    file.write(f"Координаты точек: {coordinates_points}\n")
    file.write(f"Время выполнения: {end_time - start_time:.6f} сек\n")
    file.write(f"Использование памяти: {memory[1] / 1024:.6f} КБ\n")