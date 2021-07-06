from src.components.dynamodb import dynamodb


def list_my_scores(table_name: str, uuid: str):
    item = dynamodb.find_item_by_uuid(table_name, uuid)
    return item["scores"]
