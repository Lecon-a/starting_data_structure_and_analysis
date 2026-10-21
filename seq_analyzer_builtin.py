
def seq_analyzer_builtin(numbers: list[int | float]) -> dict:
    if not numbers:
        raise ValueError("numbers must not be empty")

    total = sum(numbers)

    return {
        "mx_num": max(numbers),
        "mn_num": min(numbers),
        "_sum": total,
        "avg": total / len(numbers),
        "positive_count": sum(x > 0 for x in numbers),
        "negative_count": sum(x < 0 for x in numbers),
        "zero_count": sum(x == 0 for x in numbers),
    }
