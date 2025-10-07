def solve_vaccine(n, tA, tB, transfer_A_to_B, transfer_B_to_A):
    # dpA[i] — мин. время, чтобы закончить этап i в лаборатории A
    # dpB[i] — мин. время, чтобы закончить этап i в лаборатории B
    dpA = [0] * n
    dpB = [0] * n

    # prevA[i] — откуда пришли в A на этапе i (0=A, 1=B)
    # prevB[i] — откуда пришли в B на этапе i (0=A, 1=B)
    prevA = [-1] * n
    prevB = [-1] * n

    # Базовый случай
    dpA[0] = tA[0]
    dpB[0] = tB[0]

    # Заполняем DP
    for i in range(1, n):
        # Из A в A
        cost_A_to_A = dpA[i-1] + tA[i]
        # Из B в A
        cost_B_to_A = dpB[i-1] + transfer_B_to_A[i-1] + tA[i]

        if cost_A_to_A <= cost_B_to_A:
            dpA[i] = cost_A_to_A
            prevA[i] = 0  # пришли из A
        else:
            dpA[i] = cost_B_to_A
            prevA[i] = 1  # пришли из B

        # Из B в B
        cost_B_to_B = dpB[i-1] + tB[i]
        # Из A в B
        cost_A_to_B = dpA[i-1] + transfer_A_to_B[i-1] + tB[i]

        if cost_B_to_B <= cost_A_to_B:
            dpB[i] = cost_B_to_B
            prevB[i] = 1  # пришли из B
        else:
            dpB[i] = cost_A_to_B
            prevB[i] = 0  # пришли из A

    # Определяем минимальное время и конечную лабораторию
    if dpA[n-1] <= dpB[n-1]:
        min_time = dpA[n-1]
        current_lab = 'A'
    else:
        min_time = dpB[n-1]
        current_lab = 'B'

    # Восстанавливаем траекторию
    trajectory = [''] * n
    trajectory[n-1] = current_lab

    for i in range(n-1, 0, -1):
        if current_lab == 'A':
            from_where = prevA[i]
            if from_where == 0:
                current_lab = 'A'
            else:
                current_lab = 'B'
        else:  # current_lab == 'B'
            from_where = prevB[i]
            if from_where == 0:
                current_lab = 'A'
            else:
                current_lab = 'B'
        trajectory[i-1] = current_lab

    return min_time, trajectory


# Пример

tA = [26, 4, 6, 30]
tB = [7, 29, 14, 18]

transfer_A_to_B = [1, 6, 8]
transfer_B_to_A = [11, 1, 4]

min_time, path = solve_vaccine(4, tA, tB, transfer_A_to_B, transfer_B_to_A)

print("Минимальное время:", min_time)
print("Траектория (этап 1,2,3,4):", path)