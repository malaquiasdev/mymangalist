from src.components.dynamodb import dynamodb
from src.utils.math.calculate_average_score import calculate_average_score


def _remove_old_score_chapter(item: list, chapter_number: int) -> list:
    for score in item['scores']:
        if score['chapter_number'] == chapter_number:
            item['scores'].remove(score)

    return item


def _update_num_chapters_read(item: list, chapter_number: int) -> list:
    item['num_chapters_read'] = chapter_number
    return item


def _add_new_score(item: list, chapter_number: int, new_score: int) -> list:
    new_score_dictionary = {'chapter_number': chapter_number, 'score': new_score}
    item['scores'].append(new_score_dictionary)
    return item


def add_new_score(table_name: str, uuid: str, chapter_number: int, new_score: int):
    item = dynamodb.find_item_by_uuid(table_name, uuid)

    if not item:
        return False

    item = _remove_old_score_chapter(item, chapter_number)
    item = _update_num_chapters_read(item, chapter_number)
    item = _add_new_score(item, chapter_number, new_score)
    item['average_score'] = calculate_average_score(item['scores'])

    return dynamodb.update_item(table_name, item)
