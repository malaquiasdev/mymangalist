from src.components.dynamodb import dynamodb


def list_my_manga_scores(table_name: str, slug: str):
    manga = dynamodb.find_item_by_slug(table_name, slug)
    return manga["scores"]
