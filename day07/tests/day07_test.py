import pytest
import day07


@pytest.fixture
def tester_list():
    filename = "day07_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day07_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            line = line.replace('\n', ' ')
            return_list.append(line)
    return return_list


def test_day07_mini(tester_list):
    assert day07.total_dir_size(tester_list) == 95437


def test_day07(real_list):
    assert day07.total_dir_size(real_list) == 1141028


def test_day07_p2_mini(tester_list):
    assert day07.total_dir_size(tester_list, True) == 24933642


def test_day07_p2(real_list):
    assert day07.total_dir_size(real_list, True) == 8278005
