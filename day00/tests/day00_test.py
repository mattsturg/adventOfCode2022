import pytest
import day00


@pytest.fixture
def real_list():
    filename = "day00_in.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(int(line))
    return return_list


def test_day00(real_list):
    assert day00.print_list(real_list) == 1
