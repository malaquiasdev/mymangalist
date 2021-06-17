from src.components.dynamodb import dynamodb


def add_new_score(table_name: str, slug: str, score: dict):
    manga = dynamodb.find_manga_by_slug(table_name, slug)
    if not manga:
        return None
    manga["scores"].append(score)
    return dynamodb.update_item(table_name, manga)