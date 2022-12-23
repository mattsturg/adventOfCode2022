import pytest
import day09


@pytest.fixture
def tester_list():
    filename = "day09_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def tester_list_2():
    filename = "day09_in_0_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day09_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


def test_day09_mini(tester_list):
    assert day09.count_tail_locations(tester_list) == 13


def test_day09(real_list):
    assert day09.count_tail_locations(real_list) == 6190


def test_day09_p2_mini(tester_list_2):
    assert day09.count_chaining_tail_locations(tester_list_2) == 36


def test_day09_p2(real_list):
    assert day09.count_chaining_tail_locations(real_list) == 2516
