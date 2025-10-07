def lcs(s1, s2):
    n, m = len(s1), len(s2)
    # Создаём таблицу (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Восстанавливаем подпоследовательность
    lcs_str = []
    i, j = n, m
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()
    return dp[n][m], ''.join(lcs_str)


# Пример:
s1 = "УНИВЕРСИТЕТ"
s2 = "УНИКС"

length, subseq = lcs(s1, s2)
print(length, subseq)