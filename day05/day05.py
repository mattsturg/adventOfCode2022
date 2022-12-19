from textwrap import wrap


class Stack:
    def __init__(self, stack_in):
        count = stack_in.pop()
        stack_len = len([count[idx:idx + 4] for idx in range(0, len(count), 4)])
        self.ls = []

        for i in range(0, stack_len):
            self.ls.append([])

        for line in stack_in:
            row = [line[idx:idx + 4] for idx in range(0, len(line), 4)]
            for i, elem in enumerate(row):
                elem = elem[1]
                if not elem.isspace():
                    self.ls[i].append(elem)

        self.ls = [elem[::-1] for elem in self.ls]

    def take_instruction(self, instruct):
        instruct = instruct.split("move ")[1]
        count, instruct = instruct.split(" from ")
        start, end = instruct.split(" to ")
        for i in range(int(count)):
            temp = self.ls[int(start)-1].pop()
            self.ls[int(end)-1].append(temp)

    def take_instruction_keep_stacked(self, instruct):
        instruct = instruct.split("move ")[1]
        count, instruct = instruct.split(" from ")
        start, end = instruct.split(" to ")
        temp_ls = []
        for i in range(int(count)):
            temp = self.ls[int(start) - 1].pop()
            temp_ls.append(temp)
        temp_ls.reverse()
        self.ls[int(end) - 1].extend(temp_ls)

    def get_top_vals(self):
        top_vals = ""
        for elem in self.ls:
            top_vals = top_vals+elem.pop()
        return top_vals


def find_top_crates(in_list):
    ind = 0
    for i, elem in enumerate(in_list):
        if not elem.strip():
            ind = i
            break

    s_in = in_list[:ind]
    instructions = in_list[ind+1:]
    stack = Stack(s_in)
    for instruct in instructions:
        stack.take_instruction(instruct)
    return stack.get_top_vals()


def find_top_crates_keep_stack(in_list):
    ind = 0
    for i, elem in enumerate(in_list):
        if not elem.strip():
            ind = i
            break

    s_in = in_list[:ind]
    instructions = in_list[ind+1:]
    stack = Stack(s_in)
    for instruct in instructions:
        stack.take_instruction_keep_stacked(instruct)
    return stack.get_top_vals()
