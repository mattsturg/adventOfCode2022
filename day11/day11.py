class Monkey:
    def __init__(self, our_id, lines):
        self.id = our_id

        # parse starting items
        lines[0] = lines[0].replace("Starting items: ", "")
        self.items = []
        self.throw_id = []
        self.inspections = 0
        for num in lines[0].split(", "):
            self.items.append(int(num))
            self.throw_id.append(0)

        # parse operation
        self.operation = lines[1].replace("Operation: new = ", "")

        # parse test
        self.test = int(lines[2].replace("Test: divisible by ", ""))

        # true false
        self.true_case = int(lines[3].replace("If true: throw to monkey ", ""))
        self.false_case = int(lines[4].replace("If false: throw to monkey ", ""))

    def execute_round(self, monkey_list):
        for i, old in enumerate(self.items):
            new = eval(self.operation)//3
            self.inspections += 1
            self.items[i] = new
            if new % self.test == 0:
                self.throw_id[i] = self.true_case
            else:
                self.throw_id[i] = self.false_case
        self.throw_items(monkey_list)

    def receive_item(self, item):
        self.items.append(item)
        self.throw_id.append(0)

    def throw_items(self, monkey_list):
        for i in range(len(self.items)):
            monkey_list[self.throw_id[i]].receive_item(self.items[i])
        self.throw_id = []
        self.items = []


def monkey_business(monkeys):
    round_count = 20
    monkey_list = []
    curr_monkey_inst = []
    curr_id = 0
    for line in monkeys:
        if "Monkey" in line:
            line = line.replace("Monkey ", '')
            line = line.replace(':', '').strip()
            curr_id = int(line)
        elif not line.strip():
            monkey_list.append(Monkey(curr_id, curr_monkey_inst))
            curr_monkey_inst = []
        else:
            curr_monkey_inst.append(line.strip())
    monkey_list.append(Monkey(curr_id, curr_monkey_inst))
    for _ in range(round_count):
        for monkey in monkey_list:
            monkey.execute_round(monkey_list)
    inspection_list = []
    for monkey in monkey_list:
        inspection_list.append(monkey.inspections)
    inspection_list.sort(reverse=True)
    return inspection_list[0]*inspection_list[1]
