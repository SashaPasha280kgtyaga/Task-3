def проверить_окружение_плюсами(строка):
    длина_строки = len(строка)

    if длина_строки < 3:
        return False

    for i in range(1, длина_строки - 1):
        if строка[i].isalpha():
            if строка[i - 1] != '+' or строка[i + 1] != '+':
                return False

    return True

строка_1 = "+a+b+c+"
строка_2 = "+a+b+c"

результат_1 = проверить_окружение_плюсами(строка_1)
результат_2 = проверить_окружение_плюсами(строка_2)

print(результат_1)
print(результат_2)