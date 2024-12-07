# Домашнее задание по теме "Создание исключений"

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if 1000000 <= vin_number <= 9999999:
                return True
            else:
                raise IncorrectVinNumber(message="Некорректный диапазон для vin номера")
        else:
            raise IncorrectVinNumber(message="Некорректный тип vin номер")

    def __is_valid_numbers(self, numbers):
        if len(numbers) == 6:
            return True
        else:
            raise IncorrectCarNumbers(message="Неверная длина номера")


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"Car {first.model} успешно создан")

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"Car {second.model} успешно создан")

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"Car {third.model} успешно создан")
