from src.components.dynamodb import dynamodb
from src.utils.math.calculate_average_score import calculate_average_score


def create_new_manga_if_not_exist_in_my_list(table_name: str, slug: str, title: str, status: str, manga_status: str,
                                             num_chapters_read: int, scores: object,
                                             external_links: object) -> bool:
    average_score = calculate_average_score(scores)
    exist_in_my_list = dynamodb.find_manga_by_slug(table_name, slug)
    if not exist_in_my_list:
        dynamodb.create_new_manga(table_name, slug, title, status, manga_status, num_chapters_read, average_score,
                                  scores, external_links)
    else:
        raise ValueError(f"slug: {slug}, exist in your list")

    return True
