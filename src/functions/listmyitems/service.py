from src.components.dynamodb import dynamodb


def list_my_items(table_name: str, status: str, type: str):
    if status and type:
        return dynamodb.find_items_by_status_and_type(table_name, status, type)
    else:
        return dynamodb.find_all_items(table_name)
