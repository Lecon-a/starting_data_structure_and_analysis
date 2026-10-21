def seq_analyzer(numbers: list[int]) -> dict:
    
    # check for non-empty seq
    if not numbers:
        raise ValueError("numbers must not be empty")

    # variables declaration
    largest = numbers[0]
    smallest = numbers[0]
    _sum = numbers[0]
    avg = numbers[0]
    positive_count = 1 if numbers[0] > 0 else 0
    negative_count = 1 if numbers[0] < 0 else 0
    zero_count = 1 if numbers[0] == 0 else 0

    # I discovered that this is not necessary
    # check is the length of the seq is 1
    # if len(numbers) == 1:

    #     return {
    #         'mx_num': largest,
    #         'mn_num': smallest,
    #         '_sum': _sum,
    #         'avg': avg,
    #         'positive_count': positive_count,
    #         'negative_count': negative_count,
    #         'zero_count': zero_count
    #     }

    for i in range(1, len(numbers)):

        # compare for the greatest
        if numbers[i] > largest:
            largest = numbers[i]

        # compare for the smallest
        if numbers[i] < smallest:
            smallest = numbers[i]

        # add each element to _sum variable for index 1 to n-1
        _sum += numbers[i]

        # check for negative numbers
        if numbers[i] < 0:
            negative_count += 1
        
        # check for positive numbers
        if numbers[i] > 0:
            positive_count += 1

        # check for zero numbers
        if numbers[i] == 0:
            zero_count += 1

    avg = _sum / len(numbers)

    return {
            'mx_num': largest,
            'mn_num': smallest,
            '_sum': _sum,
            'avg': avg,
            'positive_count': positive_count,
            'negative_count': negative_count,
            'zero_count': zero_count
        }
