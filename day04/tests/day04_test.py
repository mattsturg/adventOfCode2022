import pytest
import day04


@pytest.fixture
def tester_list():
    filename = "day04_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.strip()
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day04_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.strip()
            return_list.append(line)
    return return_list


def test_day04_mini(tester_list):
    assert day04.find_contained_pairs(tester_list) == 2


def test_day04(real_list):
    assert day04.find_contained_pairs(real_list) == 453


def test_day04_p2_mini(tester_list):
    assert day04.find_overlapping_pairs(tester_list) == 4


def test_day04_p2(real_list):
    assert day04.find_overlapping_pairs(real_list) == 919
