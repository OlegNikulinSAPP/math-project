lst_in = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 1, 0, 0, 1]]

directions = [(di, dj) for di in (-1, 0, 1) for dj in (-1, 0, 1) if not (di == 0 and dj == 0)]

rows = len(lst_in)
coils = len(lst_in[0])
flag = True

for i in range(rows):
    for j in range(coils):
        if lst_in[i][j] == 1:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < coils and lst_in[ni][nj]:
                    flag = False

if flag:
    print('ДА')
else:
    print('НЕТ')
