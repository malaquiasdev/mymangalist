from src.components.dynamodb import dynamodb


def add_new_score(table_name: str, slug: str, new_score: dict):
    manga = dynamodb.find_manga_by_slug(table_name, slug)
    if not manga:
        return None
    for index, score in enumerate(manga['scores']):
        if score['chapter_number'] == new_score['chapter_number']:
            manga['scores'].pop(index)
    manga["scores"].append(new_score)
    return dynamodb.update_item(table_name, manga)
