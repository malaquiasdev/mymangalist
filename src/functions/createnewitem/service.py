from src.components.dynamodb import dynamodb


def create_new_item_if_not_exist_in_my_list(table_name: str, slug: str, title: str, status: str, type: str) -> bool:
    exist_in_my_list = dynamodb.find_item_by_slug(table_name, slug)
    if not exist_in_my_list:
        dynamodb.create_new_item(table_name, slug, title, status, type)
    else:
        raise ValueError(f"slug: {slug}, exist in your list")

    return True
