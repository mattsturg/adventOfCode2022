import pytest
import day06


@pytest.fixture
def tester_list():
    filename = "day06_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day06_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


def test_day06_mini(tester_list):
    assert day06.find_marker(tester_list, 4) == 7


def test_day06(real_list):
    assert day06.find_marker(real_list, 4) == 1707


def test_day06_p2_mini(tester_list):
    assert day06.find_marker(tester_list, 14) == 19


def test_day06_p2(real_list):
    assert day06.find_marker(real_list, 14) == 3697
