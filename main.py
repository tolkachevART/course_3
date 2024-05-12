from settings import OPERATION_PATH
from src.utils import load_json, get_executed_operations, sort_operations_by_date, format_date, mask_card_number

operations = load_json(OPERATION_PATH)
executed_operations = get_executed_operations(operations)
sort_operations = sort_operations_by_date(executed_operations)
for op in sort_operations[:5]:
    print(f"{format_date(op['date'])}  {op['description']}")
    from_masked = mask_card_number(op['from']) if 'from' in op else ""
    to_masked = mask_card_number(op['to']) if 'to' in op else ""

    if from_masked:
        print(f"{from_masked} -> {to_masked}")
    else:
        print(f"{to_masked}")
    print(f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}")
    print()
