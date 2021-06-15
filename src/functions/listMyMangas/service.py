from src.components.dynamodb import dynamodb


def list_my_mangas(table_name: str, status: str):
    if status:
        return dynamodb.find_mangas_by_status(table_name, status)
    else:
        return dynamodb.find_all_mangas(table_name)
