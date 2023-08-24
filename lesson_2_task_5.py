def month_to_season(month_number):
    if 1 <= month_number <= 2 or month_number == 12:
        return "Зима"
    elif 3 <= month_number <= 5:
        return "Весна"
    elif 6 <= month_number <= 8:
        return "Лето"
    elif 9 <= month_number <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"

month_number = int(input("Введите номер месяца: "))
season = month_to_season(month_number)
print(season)