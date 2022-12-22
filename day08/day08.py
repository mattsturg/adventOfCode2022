class Forest:
    def __init__(self, height_list):
        self.tree_heights = []
        self.tree_visible = []
        self.tree_count = []
        for i in range(len(height_list)):
            self.tree_heights.append([])
            self.tree_visible.append([])
            self.tree_count.append([])
        for i, line in enumerate(height_list):
            line = line.strip()
            for num in line:
                num = int(num)
                self.tree_heights[i].append(num)
                self.tree_visible[i].append(False)
                self.tree_count[i].append(1)

    def scenic_score_look_left(self):
        for i in range(len(self.tree_heights)):
            for j in range(len(self.tree_heights[i])):
                our_height = self.tree_heights[i][j]
                count_visible_trees = 0
                temp_j = j-1
                while temp_j > -1:
                    count_visible_trees += 1
                    if our_height <= self.tree_heights[i][temp_j]:
                        break
                    temp_j -= 1
                self.tree_count[i][j] *= count_visible_trees

    def rotate_lists(self):
        self.tree_visible = list(zip(*self.tree_visible))[::-1]
        for i in range(len(self.tree_visible)):
            self.tree_visible[i] = list(self.tree_visible[i])
        self.tree_heights = list(zip(*self.tree_heights))[::-1]
        for i in range(len(self.tree_heights)):
            self.tree_heights[i] = list(self.tree_heights[i])
        self.tree_count = list(zip(*self.tree_count))[::-1]
        for i in range(len(self.tree_count)):
            self.tree_count[i] = list(self.tree_count[i])

    def check_visible_from_left(self):
        for i, row in enumerate(self.tree_heights):
            max_height = -1
            for j, height in enumerate(row):
                if height > max_height:
                    self.tree_visible[i][j] = True
                    max_height = height

    def sum_visible(self):
        total = 0
        for row in self.tree_visible:
            for vis in row:
                if vis:
                    total += 1
        return total

    def max_scenic_score(self):
        max_score = 0
        for row in self.tree_count:
            temp_max = max(row)
            if temp_max > max_score:
                max_score = temp_max
        return max_score


def visible_trees(height_list):
    our_forest = Forest(height_list)
    our_forest.check_visible_from_left()
    for i in range(3):
        our_forest.rotate_lists()
        our_forest.check_visible_from_left()
    return our_forest.sum_visible()


def scenic_score(height_list):
    our_forest = Forest(height_list)
    our_forest.scenic_score_look_left()
    for i in range(3):
        our_forest.rotate_lists()
        our_forest.scenic_score_look_left()
    return our_forest.max_scenic_score()
