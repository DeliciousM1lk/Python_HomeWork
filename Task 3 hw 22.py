def set_gen(numbers):
    result_set = set()
    occurrences = {}

    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    for num, count in occurrences.items():
        for i in range(1, count + 1):
            if i == 1:
                result_set.add(num) 
            else:
                result_set.add(str(num) * i)

    return result_set

numbers = [4, 2, 4, 3, 4, 2]
result = set_gen(numbers)
print(result)
