def count_happy_numbers(length):
    if length <= 0:
        return "Длина должна быть положительным числом."

    count = 0

    for left_sum in range(1, 10 * length // 2):  
        for left_combination in get_digit_combinations(length, left_sum):
            right_sum = left_sum  
            for right_combination in get_digit_combinations(length, right_sum):
                count += 1

    return count


def get_digit_combinations(length, target_sum, prefix=''):
    if length == 1:
        if 0 <= target_sum <= 9:
            return [prefix + str(target_sum)]
        else:
            return []

    combinations = []
    for digit in range(10):
        new_prefix = prefix + str(digit)
        new_target_sum = target_sum - digit
        if 0 <= new_target_sum <= 9:
            combinations += get_digit_combinations(length - 1, new_target_sum, new_prefix)

    return combinations
length = int(input("Введите длину числа: "))
result = count_happy_numbers(length)
print(f"Количество счастливых чисел длины {length}: {result}")