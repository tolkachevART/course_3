import json
from datetime import datetime
from pathlib import Path


def load_json(path: Path) -> list[dict]:
    """Загружает JSON файл и возвращает список объектов"""
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    """Возвращает список операций в состоянии EXECUTED."""
    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
    ]


def sort_operations_by_date(operations: list[dict]) -> list[dict]:
    """Сортирует операции по дате."""
    return sorted(operations, key=lambda operation: operation['date'], reverse=True)


def format_date(date: str) -> str:
    """Форматирует дату в соответствии с временем."""
    iso_date = datetime.fromisoformat(date)
    return iso_date.strftime('%d.%m.%Y')


def mask_card_number(card_number):
    """
    Возвращает замаскированные номера счетов
    и карт отправителя/получателя .
    """
    if 'Счет' in card_number:
        masked_number = card_number[:5] + '**' + card_number[-4:]
        return masked_number

    else:
        masked_number = card_number[:-16] + card_number[-16:-12] + ' ' + \
                        card_number[-12:-10] + '** **** ' + card_number[-4:]
        return masked_number
