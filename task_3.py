def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
def main():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()
        n = int(lines[0].strip())
        a = list(map(int,lines[1].strip().split()))
        b = list(map(int,lines[2].strip().split()))

        bubble_sort(a)
        bubble_sort(b)

        max = 0
        for i in range(n):
            max += a[i]*b[i]

        with open("output.txt","w") as file:
            file.write(str(max) + "\n")

    except Exception as e:
        print("Ошибка:", e)

if __name__=="__main__":
    main()