lst_in = [8, 6, 1, 2, -1, 10, 0, 4]

for i in range(len(lst_in)):
    min_id = i
    for j in range(i + 1, len(lst_in)):
        if lst_in[j] < lst_in[min_id]:
            min_id = j
    lst_in[i], lst_in[min_id] = lst_in[min_id], lst_in[i]

print(lst_in)
