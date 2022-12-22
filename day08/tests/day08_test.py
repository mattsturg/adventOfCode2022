import pytest
import day08


@pytest.fixture
def tester_list():
    filename = "day08_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day08_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


def test_day08_mini(tester_list):
    assert day08.visible_trees(tester_list) == 21


def test_day08(real_list):
    assert day08.visible_trees(real_list) == 1776


def test_day08_p2_mini(tester_list):
    assert day08.scenic_score(tester_list) == 8


def test_day08_p2(real_list):
    assert day08.scenic_score(real_list) == 234416
