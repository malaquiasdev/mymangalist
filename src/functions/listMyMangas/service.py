from src.components.dynamodb import dynamodb


def list_my_mangas(table_name: str, status: str):
    return dynamodb.find_mangas_by_status(table_name, status)
