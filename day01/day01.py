def count_calories(calories_list):
    elf_calories = []
    i = 0

    curr_cal = 0
    for i in range(len(calories_list)):
        if calories_list[i] != '\n':
            curr_cal += int(calories_list[i])
            continue
        else:
            elf_calories.append(curr_cal)
            curr_cal = 0
    return max(elf_calories)


def count_top_three_calories(calories_list):
    elf_calories = []
    i = 0

    curr_cal = 0
    for i in range(len(calories_list)):
        if calories_list[i] != '\n':
            curr_cal += int(calories_list[i])
            continue
        else:
            elf_calories.append(curr_cal)
            curr_cal = 0
        elf_calories.sort(reverse=True)
        top_three = elf_calories[:3]
        s = 0
        for elem in top_three:
            s += elem
    return s
