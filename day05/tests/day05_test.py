import pytest
import day05


@pytest.fixture
def tester_list():
    filename = "day05_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day05_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


def test_day05_mini(tester_list):
    assert day05.find_top_crates(tester_list) == "CMZ"


def test_day05(real_list):
    assert day05.find_top_crates(real_list) == "BWNCQRMDB"


def test_day05_p2_mini(tester_list):
    assert day05.find_top_crates_keep_stack(tester_list) == "MCD"


def test_day05_p2(real_list):
    assert day05.find_top_crates_keep_stack(real_list) == "NHWZCBNBF"
