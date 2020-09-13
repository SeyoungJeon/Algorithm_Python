def solution(n, s, a, b, fares):
    MAX_VALUE = float('inf')

    dist = [[0] * n for i in range(n)]

    giography = []
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j:
                temp.append(0)
            else:
                temp.append(MAX_VALUE)
        giography.append(temp)

    for c, d, f in fares:
        giography[c-1][d-1] = f
        giography[d-1][c-1] = f

    for i in range(n):
        for j in range(n):
            dist[i][j] = giography[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    score = []
    for i in range(n):
        duplicated_value = dist[s-1][i]
        score.append(duplicated_value + dist[i][a-1] + dist[i][b-1])

    return min(score)

print(solution(6, 4, 6, 2, [[4, 1, 10], [4, 2, 66], [4, 6, 50], [1, 3, 41], [1, 5, 24], [1, 6, 25], [2, 3, 22], [3, 5, 24], [5, 6, 2]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
