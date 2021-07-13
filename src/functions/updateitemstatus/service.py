from src.components.dynamodb import dynamodb


def update_item_status(table_name: str, uuid: str, status: str) -> bool:
    item = dynamodb.find_item_by_uuid(table_name, uuid)

    if not item:
        return False

    item['status'] = status

    return dynamodb.update_item(table_name, item)
