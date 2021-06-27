from decimal import *
import typing

ROUNDING_VALUE_TO_ONE = 1


def calculate_average_score(scores: typing.List[dict]) -> Decimal:
    total_score = 0
    for item in scores:
        total_score = total_score + item["score"]

    return Decimal(round(total_score / len(scores), ROUNDING_VALUE_TO_ONE))
