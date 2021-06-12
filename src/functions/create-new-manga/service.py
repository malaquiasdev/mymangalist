from src.components.dynamodb import dynamodb


def create_new_manga_if_not_exist_in_my_list(table_name: str, slug: str, title: str, status: str, manga_status: str,
                                             num_chapters_read: int, average_score: float, scores: object,
                                             external_links: object) -> bool:
    exist_in_my_list = dynamodb.find_manga_by_slug(table_name, slug)
    if not exist_in_my_list:
        dynamodb.create_new_manga(table_name, slug, title, status, manga_status, num_chapters_read, average_score,
                                  scores, external_links)
    else:
        raise Exception(f"slug: {slug}, exist in your list")

    return True
