class Directory:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.size = 0
        self.children = []

    def match_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return -1

    def set_children(self, child_ls):
        for line in child_ls:
            split_line = line.split()
            if split_line[0] != "dir":
                self.size += int(split_line[0])
            else:
                child_dir = Directory(split_line[1], self)
                self.children.append(child_dir)

    def eval_size(self):
        for child in self.children:
            self.size += child.eval_size()
        return self.size

    def get_root(self):
        if not self.parent:
            return self
        else:
            return self.parent.get_root()

    def get_sum_under(self, val):
        s = 0
        for child in self.children:
            s += child.get_sum_under(val)
        if self.size < val:
            s += self.size
        return s

    def search_min_del(self, mem_needed):
        del_dir = None
        for child in self.children:
            temp_del = child.search_min_del(mem_needed)
            if not del_dir:
                del_dir = temp_del
            elif temp_del and temp_del < del_dir:
                del_dir = temp_del
        if not del_dir:
            if self.size > mem_needed:
                return self.size
            else:
                return del_dir
        if mem_needed < self.size < del_dir:
            return self.size
        return del_dir


def parse_term(term_list):
    temp_dir = None
    temp_line_list = []
    for line in term_list:
        if line.strip() == "$ ls":
            continue
        elif "$ cd" in line:
            if temp_dir:
                temp_dir.set_children(temp_line_list)
                temp_line_list = []
            val = line.split("$ cd")[1].strip()
            if val != "..":
                if not temp_dir:
                    temp_dir = Directory(val, None)
                else:
                    temp_dir = temp_dir.match_child(val)
            else:
                temp_dir = temp_dir.parent
        else:
            temp_line_list.append(line)
    temp_dir.set_children(temp_line_list)
    temp_dir = temp_dir.get_root()
    temp_dir.eval_size()
    return temp_dir


def total_dir_size(term_out, p2=False):
    root_dir = parse_term(term_out)
    if p2:
        unused_space = 30000000
        total_space = 70000000
        needed_space = unused_space - (total_space - root_dir.size)
        return root_dir.search_min_del(needed_space)
    else:
        return root_dir.get_sum_under(100000)
