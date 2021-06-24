from src.components.dynamodb import dynamodb


def list_my_scores(table_name: str, slug: str):
    item = dynamodb.find_item_by_slug(table_name, slug)
    return item["scores"]
