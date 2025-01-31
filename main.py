p_list = ["п", "ф", "а", "я", "о", "б"]

print(p_list)
print(len(p_list))
while True:  # сортировка символов
    cycle = 0
    for i in range(len(p_list) - 1):
        if p_list[i][1] < p_list[i + 1][1] or (p_list[i][0] > p_list[i + 1][0] and p_list[i][1] == p_list[i + 1][1]):
            p_list[i], p_list[i + 1] = p_list[i + 1], p_list[i]
            cycle += 1
    if cycle == 0:
        break

print(p_list)
