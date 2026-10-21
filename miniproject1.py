def seq_analyzer(numbers: list[int]) -> dict:
    
    # check for non-empty seq
    if not numbers:
        raise ValueError("numbers must not be empty")

    # variables declaration
    largest = numbers[0]
    smallest = numbers[0]
    _sum = numbers[0]
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

    for i in range(1, len(numbers)): # O(n)

        number = numbers[i]

        # compare for the greatest
        if number > largest: 
            largest = number

        # compare for the smallest
        if number < smallest: 
            smallest = number

        # add each element to _sum variable for index 1 to n-1
        _sum += number 

        # check for negative numbers
        # check for positive numbers
        # check for zero numbers
        if number < 0: 
            negative_count += 1
        elif number > 0: 
            positive_count += 1
        else:
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
