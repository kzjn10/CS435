# Subset sum with one solition
def subset(s: list[int], n: int):
    rows = len(s)
    res = [[' ' for _ in range(n + 1)] for _ in range(rows)]
    for i in range(rows):
        for j in range(n + 1):
            if j == 0:
                res[i][j] = '{}'
                continue

            if i == 0:
                if j == s[i]:
                    res[i][j] = '{' + f'{s[i]}' + '}'
            else:
                if j < s[i]:
                    if res[i][j] == ' ':
                        res[i][j] = '' + res[i - 1][j] + ''
                    else:
                        res[i][j] = '' + res[i - 1][j] + ''
                else:
                    if res[i - 1][j - s[i]] == ' ':
                        res[i][j] = ' '
                    elif res[i - 1][j - s[i]] != ' ':
                        if len(res[i - 1][j - s[i]]) == 2:
                            if j == s[i] and len(res[i - 1][j]) > 2:
                                res[i][j] = '' + res[i - 1][j]
                            else:
                                res[i][j] = '' + res[i - 1][j - s[i]].replace('}', '') + f'{s[i]}' + '}'
                        else:
                            res[i][j] = '' + res[i - 1][j - s[i]].replace('}', ',') + f'{s[i]}' + '}'

            # Enter new line

    # -------- Print test value --------
    t = '['
    for i in range(n + 1):
        t += f"{str(i):>3}"
    print(f"--   {t}]")
    for i in range(rows):
        t = f'-- {s[i]} ['
        for j in range(n + 1):
            t = t + str(res[i][j])
            if j < n:
                t = t + ', '

        print(f"{t}]")


subset([3, 4, 7, 8], 15)
