import pytest
import day11


@pytest.fixture
def tester_list():
    filename = "day11_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day11_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


def test_day11_mini(tester_list):
    assert day11.monkey_business(tester_list) == 10605


def test_day11(real_list):
    assert day11.monkey_business(real_list) == 13740


# def test_day11_p2_mini(tester_list_2):
#     assert day11.count_chaining_tail_locations(tester_list_2) == 36
#
#
# def test_day11_p2(real_list):
#     assert day11.count_chaining_tail_locations(real_list) == 2516
