def is_busted(card_values):
    total_value = sum(card_values)
    return total_value > 21
card_values = [10, 5, 7] 
result = is_busted(card_values)
if result:
    print("Перебор! (сумма больше 21)")
else:
    print("Не перебор (сумма меньше или равна 21)")