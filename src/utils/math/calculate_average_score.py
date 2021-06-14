import typing


def calculate_average_score(scores: typing.List[dict]) -> float:
    total_score = 0
    for item in scores:
        total_score = total_score + item["score"]

    return total_score / len(scores)
