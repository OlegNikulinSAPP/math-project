lst_in = list(map(int, input().split()))

for i in range(len(lst_in) - 1):
    for j in range(len(lst_in) - i - 1):
        if lst_in[j] > lst_in[j + 1]:
            lst_in[j], lst_in[j + 1] = lst_in[j + 1], lst_in[j]

print(lst_in)