class Processor:
    def __init__(self):
        self.is_working_add = False
        self.step = 0
        self.x = 1
        self.v = 0
        self.print_screen = []

    def take_ins(self, instructions):
        self.step += 1
        get_ret = self.check_strength()
        if "noop" in instructions:
            return get_ret
        else:
            _, val = instructions.split()
            self.is_working_add = True
            self.v = int(val)
        return get_ret

    def finish_add(self):
        self.step += 1
        get_ret = self.check_strength()
        self.x += self.v
        self.is_working_add = False
        return get_ret

    def check_strength(self):
        self.output_cycle()
        if (self.step - 20) % 40 == 0:
            return self.step * self.x
        return 0

    def output_cycle(self):

        dist = ((self.step-1) % 40) - self.x
        if abs(dist) < 2:
            if self.step % 40 == 0:
                self.print_screen.append("#\n")
            else:
                self.print_screen.append("#")
        else:
            if self.step % 40 == 0:
                self.print_screen.append(".\n")
            else:
                self.print_screen.append(".")


def calc_signal_strength(instruct_ls):
    print()
    p = Processor()
    s = 0
    for line in instruct_ls:
        if p.is_working_add:
            s += p.finish_add()
        s += p.take_ins(line)
    for val in p.print_screen:
        print(val, end='')
    return s
