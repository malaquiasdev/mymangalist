from src.components.dynamodb import dynamodb


def search_by(table_name: str, title: str):
    items = dynamodb.find_items_by_title(table_name, title)

    if not items:
        return []

    return items
