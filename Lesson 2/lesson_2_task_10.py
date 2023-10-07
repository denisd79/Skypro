def bank(X, Y):
    interest_rate = 0.10  # Годовая процентная ставка
    total_amount = X  # Начальная сумма вклада

    for _ in range(Y):
        total_amount += total_amount * interest_rate  # Увеличиваем сумму на проценты

    return total_amount

# Пример использования функции
X = float(input("Введите размер вклада: "))
Y = int(input("Введите срок вклада (лет): "))
final_amount = bank(X, Y)
print("Сумма на счету через", Y, "лет:", final_amount)