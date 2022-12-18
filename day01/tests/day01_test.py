import pytest
import day01


@pytest.fixture
def tester_list():
    filename = "day01_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day01_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day00_mini(tester_list):
    assert day01.count_calories(tester_list) == 24000


def test_day00(real_list):
    assert day01.count_calories(real_list) == 68802


def test_day00_p2(real_list):
    assert day01.count_top_three_calories(real_list) == 205370
