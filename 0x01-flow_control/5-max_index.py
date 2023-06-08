Lst = [1, 15, 2, 38, 48, 7, 16, 44]

max_num = Lst[0]
max_index = 0

for a in range(1, len(Lst)):
    if Lst[a] > max_num:
        max_num = Lst[a]
        max_index = 1
print(f"Max is {max_num} at Index {max_index}")


