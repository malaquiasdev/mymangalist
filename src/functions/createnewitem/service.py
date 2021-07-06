import uuid
from src.components.dynamodb import dynamodb


def create_new_item_if_not_exist_in_my_list(table_name: str, slug: str, title: str, status: str, type: str) -> bool:
    exist_in_my_list = dynamodb.find_items_by_title_and_type(table_name, slug, type)
    if not exist_in_my_list:
        dynamodb.create_new_item(table_name, uuid.uuid4().hex, title, status, type)
    else:
        raise ValueError(f"title: {title}, exist in your list")

    return True
