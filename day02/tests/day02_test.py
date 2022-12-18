import pytest
import day02


@pytest.fixture
def tester_list():
    filename = "day02_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day02_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day02_mini(tester_list):
    assert day02.make_players(tester_list) == 15


def test_day02(real_list):
    assert day02.make_players(real_list) == 13675


def test_day02_p2_mini(tester_list):
    assert day02.make_players_wl(tester_list) == 12


def test_day02_p2(real_list):
    assert day02.make_players_wl(real_list) == 14184
