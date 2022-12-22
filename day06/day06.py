def check_match(four_letters):
    for let in four_letters:
        if four_letters.count(let) > 1:
            return False
        elif not let:
            return False
    return True


def find_marker(data_stream, r):
    last_four = []
    for i in range(r):
        last_four.append('')
    for ind, letter in enumerate(data_stream[0]):
        last_four.pop(0)
        last_four.append(letter)
        if check_match(last_four):
            return ind+1
    return -1
