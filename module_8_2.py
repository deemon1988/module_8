# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"
from logging import raiseExceptions


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {i}")

    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        data = personal_sum(numbers)
        summ_numbers = data[0]
        avg_numbers = summ_numbers / (len(numbers) - data[1])
        return avg_numbers
    except ZeroDivisionError as exc:
        print(f"{exc} - количество чисел = 0")
        return 0
    except TypeError as ex:
        print(f"{ex} - В numbers записан некорректный тип данных")




print(calculate_average("1, 2, 3"))
print(calculate_average([1, "Строка", 3, "Ещё Строка"]))
print(calculate_average(567))
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')


