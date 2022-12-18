def find_duplicate(sack_list):
    s = 0
    for line in sack_list:
        line = line.strip()
        our_letter = ''
        let_list = []
        half = len(line)//2
        first_half = line[:half]
        second_half = line[half:]

        for letter in first_half:
            let_list.append(letter)

        for letter in second_half:
            if letter in let_list:
                our_letter = letter

        if ord(our_letter) > 96:
            s += ord(our_letter) - 96
        else:
            s += ord(our_letter) - 38
    return s


def find_group(sack_list):
    s = 0
    for ind in range(0, len(sack_list), 3):
        let_list = []
        for offset in range(3):
            temp = []
            line = sack_list[ind + offset].strip()
            for letter in line:
                if offset == 0:
                    temp.append(letter)
                else:
                    if letter in let_list:
                        temp.append(letter)

            let_list = temp
        our_letter = let_list[0]

        if ord(our_letter) > 96:
            s += ord(our_letter) - 96
        else:
            s += ord(our_letter) - 38
    return s
