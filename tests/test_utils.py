from pathlib import Path

import pytest

from src.utils import format_date, get_executed_operations, mask_card_number, sort_operations_by_date, load_json


def test_invalid_file_path():

    with pytest.raises(FileNotFoundError):
        load_json(Path("invalid_path.json"))


def test_returns_list_of_executed_operations():
    operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "FAILED"},
        {}
    ]

    result = get_executed_operations(operations)

    assert result == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]


def test_returns_empty_list():
    assert get_executed_operations([]) == []


def test_valid_date_formatting():
    input_date = '2022-01-01'
    expected_output = '01.01.2022'

    actual_output = format_date(input_date)

    assert actual_output == expected_output


def test_sort_operations_by_date_empty_list():
    operations = []

    expected_result = []

    result = sort_operations_by_date(operations)

    assert result == expected_result


def test_empty_date_string():
    input_date = ''

    with pytest.raises(ValueError):
        format_date(input_date)


def test_sort_operations_by_date_descending_order():
    operations = [
        {'date': '2022-01-01', 'operation': 'A'},
        {'date': '2022-03-01', 'operation': 'C'},
        {'date': '2022-02-01', 'operation': 'B'}
    ]

    expected_result = [
        {'date': '2022-03-01', 'operation': 'C'},
        {'date': '2022-02-01', 'operation': 'B'},
        {'date': '2022-01-01', 'operation': 'A'}
    ]

    result = sort_operations_by_date(operations)

    assert result == expected_result


def test_sort_operations_by_date_invalid_input():
    operations = "not a list"

    with pytest.raises(TypeError):
        sort_operations_by_date(operations)


def test_mask_card_number_1():
    card_number = '1234567890123456'

    result = mask_card_number(card_number)

    assert result == '1234 56** **** 3456'
