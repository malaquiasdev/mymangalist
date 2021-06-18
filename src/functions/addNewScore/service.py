from src.components.dynamodb import dynamodb
from src.utils.math.calculate_average_score import calculate_average_score


def add_new_score(table_name: str, slug: str, new_score: dict):
    manga = dynamodb.find_manga_by_slug(table_name, slug)
    if not manga:
        return False
    for index, score in enumerate(manga['scores']):
        if score['chapter_number'] == new_score['chapter_number']:
            manga['scores'].pop(index)
    manga["num_chapters_read"] = new_score["chapter_number"]
    manga["scores"].append(new_score)
    manga["average_score"] = calculate_average_score(manga["scores"])
    return dynamodb.update_item(table_name, manga)
