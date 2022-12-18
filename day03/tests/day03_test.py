import pytest
import day03


@pytest.fixture
def tester_list():
    filename = "day03_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day03_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day03_mini(tester_list):
    assert day03.find_duplicate(tester_list) == 157


def test_day03(real_list):
    assert day03.find_duplicate(real_list) == 7917


def test_day03_p2_mini(tester_list):
    assert day03.find_group(tester_list) == 70


def test_day03_p2(real_list):
    assert day03.find_group(real_list) == 2585
