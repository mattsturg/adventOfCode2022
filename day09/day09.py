class Rope:
    def __init__(self):
        self.visited_spots = [[0, 0]]
        self.head_location = [0, 0]
        self.tail_location = [0, 0]
        self.direction_dict = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}

    def take_instructions(self, ins):
        direction, dist = ins.split()
        for _ in range(int(dist)):
            # Move head
            dir_val = self.direction_dict[direction]
            self.head_location = [dir_val[0] + self.head_location[0], dir_val[1] + self.head_location[1]]

            # Adjust tail
            self.move_tail()

    def move_tail(self):
        # Check head adjacency
        if self.head_location[0] in range(self.tail_location[0]-1, self.tail_location[0]+2) and \
                self.head_location[1] in range(self.tail_location[1]-1, self.tail_location[1]+2):
            return
        else:
            # not adjacent
            if self.head_location[0] > self.tail_location[0]:
                self.tail_location[0] += 1
            elif self.head_location[0] < self.tail_location[0]:
                self.tail_location[0] -= 1

            if self.head_location[1] > self.tail_location[1]:
                self.tail_location[1] += 1
            elif self.head_location[1] < self.tail_location[1]:
                self.tail_location[1] -= 1

        # Check new tail spot
        if self.tail_location not in self.visited_spots:
            self.visited_spots.append(self.tail_location[:])


class LinkedRope:
    def __init__(self, rope):
        self.head_location = [0, 0]
        self.tail_rope = rope
        self.tail_location = [0, 0]
        self.direction_dict = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}

    def move_tail(self):
        # Check head adjacency
        if self.head_location[0] in range(self.tail_location[0]-1, self.tail_location[0]+2) and \
                self.head_location[1] in range(self.tail_location[1]-1, self.tail_location[1]+2):
            return
        else:
            # not adjacent
            if self.head_location[0] > self.tail_location[0]:
                self.tail_location[0] += 1
            elif self.head_location[0] < self.tail_location[0]:
                self.tail_location[0] -= 1

            if self.head_location[1] > self.tail_location[1]:
                self.tail_location[1] += 1
            elif self.head_location[1] < self.tail_location[1]:
                self.tail_location[1] -= 1
        self.tail_rope.head_location = self.tail_location
        self.tail_rope.move_tail()

    def get_tail(self):
        temp = self.tail_rope
        while isinstance(temp, LinkedRope):
            temp = temp.tail_rope
        return temp


def count_tail_locations(move_list):
    our_rope = Rope()
    our_rope.move_tail()
    for line in move_list:
        our_rope.take_instructions(line)
    return len(our_rope.visited_spots)


def count_chaining_tail_locations(move_list):
    length = 10
    last_rope = Rope()
    for i in range(length-2):
        last_rope = LinkedRope(last_rope)
    for line in move_list:
        last_rope.take_instructions(line)
    return len(last_rope.get_tail().visited_spots)
