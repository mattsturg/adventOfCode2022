import pytest
import day10


@pytest.fixture
def tester_list():
    filename = "day10_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day10_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


def test_day10_mini(tester_list):
    assert day10.calc_signal_strength(tester_list) == 13140


def test_day10(real_list):
    assert day10.calc_signal_strength(real_list) == 13740


# def test_day10_p2_mini(tester_list_2):
#     assert day10.count_chaining_tail_locations(tester_list_2) == 36
#
#
# def test_day10_p2(real_list):
#     assert day10.count_chaining_tail_locations(real_list) == 2516
