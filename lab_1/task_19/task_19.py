def matrix(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for lenght in range(2, n + 1):
        for i in range(n - lenght + 1):
            j = i + lenght - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                current_cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if current_cost < dp[i][j]:
                    dp[i][j] = current_cost
                    split[i][j] = k

    def build(i, j):
        if i == j:
            return f"А"
        else:
            left = build(i, split[i][j])
            right = build(split[i][j] + 1, j)
            return f"({left}{right})"
    return build(0, n - 1)


with open('input.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())
p = []
for line in lines[1:n + 1]:
    a, b = map(int, line.strip().split())
    p.append(a)
p.append(b)

result = matrix(p)

with open('output.txt', 'w') as file:
    file.write(result)

