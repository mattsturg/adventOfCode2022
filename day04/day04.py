class Elf:
    def __init__(self, parse):
        temp = parse.split('-')
        self.start = int(temp[0])
        self.finish = int(temp[1])

    def contains_time(self, other_elf):
        if self.start <= other_elf.start and self.finish >= other_elf.finish:
            return True
        return False

    def overlaps_with(self, other_elf):
        if self.start <= other_elf.finish and self.finish >= other_elf.start:
            return True
        return False


def find_contained_pairs(pair_list):
    total = 0
    for line in pair_list:
        temp = line.split(',')
        elf1 = Elf(temp[0])
        elf2 = Elf(temp[1])

        if elf1.contains_time(elf2) or elf2.contains_time(elf1):
            total += 1
    return total


def find_overlapping_pairs(pair_list):
    total = 0
    for line in pair_list:
        temp = line.split(',')
        elf1 = Elf(temp[0])
        elf2 = Elf(temp[1])

        if elf1.overlaps_with(elf2) or elf2.overlaps_with(elf1):
            total += 1
    return total
