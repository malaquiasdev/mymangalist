from decimal import *
from src.components.dynamodb import dynamodb
from src.utils.math.calculate_average_score import calculate_average_score


def add_new_score(table_name: str, slug: str, chapter_number: int, score: float):
    item = dynamodb.find_item_by_slug(table_name, slug)
    if not item:
        return False
    for index, score in enumerate(item['scores']):
        if score['chapter_number'] == chapter_number:
            item['scores'].pop(index)
    item['num_chapters_read'] = chapter_number
    new_score_dictionary = {'chapter_number': chapter_number, 'score': Decimal(score)}
    item['scores'].append(new_score_dictionary.copy())
    item['average_score'] = calculate_average_score(item['scores'])
    return dynamodb.update_item(table_name, item)
