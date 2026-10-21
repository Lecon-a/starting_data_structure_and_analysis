
from typing import TypedDict


class SequenceStats(TypedDict):
    mx_num: int | float
    mn_num: int | float
    _sum: int | float
    avg: float
    positive_count: int
    negative_count: int
    zero_count: int


def seq_analyzer(numbers: list[int | float]) -> SequenceStats:
    """Analyse a non-empty list of integers or floats."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = smallest = total = numbers[0]
    positive_count = int(numbers[0] > 0)
    negative_count = int(numbers[0] < 0)
    zero_count = int(numbers[0] == 0)

    for i in range(1, len(numbers)):

        number = numbers[i]
        
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

        total += number

        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    return {
        "mx_num": largest,
        "mn_num": smallest,
        "_sum": total,
        "avg": total / len(numbers),
        "positive_count": positive_count,
        "negative_count": negative_count,
        "zero_count": zero_count,
    }
