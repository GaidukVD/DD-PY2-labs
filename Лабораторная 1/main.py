import doctest


class Auto:
    def __init__(self, brand_name: str, model_name, mileage: int, gas: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param brand_name: Марка авто
        :param model_name: Модель авто
        :param mileage: Пробег в км
        :param mileage: Количество топлива в литрах

        Примеры:
        >>> auto = Auto(Ford, Aerostar, 140252, 23.42)  # инициализация экземпляра класса
        """
        if not isinstance(brand_name, str):
            raise TypeError("Название марки авто должно быть типа str")
        if not isinstance(model_name, (str, int)):
            raise TypeError("Название модели авто должно быть типа str или int")
        if not isinstance(mileage, int):
            raise TypeError("Пробег авто должен быть типа int")
        if mileage <= 0:
            raise ValueError("Пробег должен быть положительным числом")
        self.brand_name = brand_name
        self.model_name = model_name
        self.mileage = mileage
        self.gas = gas

    def is_empty_tank(self) -> bool:
        """
        Функция которая проверяет пусть ли бак
        :return: Является ли бак пустым
        Примеры:
        >>> car = Auto(Lada, 2101, 43000, 0)
        >>> car.is_empty_tank()
        """
        ...

    def add_km_to_odometer(self, trip: int) -> None:
        """
        Добавление пробега.
        :param trip: Количество километров, с момента прошлой записи пробега (трип)
        Примеры:
        >>> car = Auto(Lada, 2101, 43000, 0)
        >>> car.add_km_to_odometer(2588)
        """
        if not isinstance(trip, int):
            raise TypeError("Добавляемый километраж должен быть типа int")
        if trip < 0:
            raise ValueError("Добавляемый километраж должен быть положительным числом")
        ...

    class Garage:
        def __init__(self, parking_spaces: int, occupied_parking_spaces: int):
            """
            Создание и подготовка к работе объекта "Гараж"
            :param parking_spaces: Общее количесвто мест в гараже/парковке
            :param occupied_parking_spaces: занятых мест

            Примеры:
            >>> garage = Garage(5, 2)  # инициализация экземпляра класса
            """
            if not isinstance(occupied_parking_spaces, int):
                raise TypeError("Количество занятых мест для авто должно быть типа int")
            if parking_spaces <= 0:
                raise ValueError("Количество занятых мест для авто должно быть положительным числом")
            if not isinstance(parking_spaces, int):
                raise TypeError("Количество мест для авто должно быть типа int")
            if parking_spaces <= 0:
                raise ValueError("Количество мест для авто должно быть положительным числом")
            if occupied_parking_spaces > parking_spaces:
                raise ValueError("Количество занятых мест для авто должно быть не больше общего количества мест в гараже")
            self.parking_spaces = parking_spaces
            self.occupied_parking_spaces = occupied_parking_spaces

        def is_garage_free(self) -> bool:
            """
            Функция которая проверяет пуст ли гараж
            :return: Является ли гараж пустым
            Примеры:
            >>> garage = Garage(230, 0)
            >>> garage.is_garage_free()
            """
            ...

        def add_cars_to_garage(self, add_cars: int) -> None:
            """
            Добавление автомобилей в гараж.
            :param add_cars: Количество машин, которые заезжают в гараж
            :raise ValueError: Если количество добавляемых авто превышает количество свободных мест в гараже, то вызываем ошибку
            Примеры:
            >>> garage = Garage(15, 14 )
            >>> garage.add_cars_to_garage(3)
            """
            if not isinstance(add_cars, int):
                raise TypeError("Количество авто должно быть типа int")
            if add_cars <= 0:
                raise ValueError("Количество авто должно быть положительным числом")
            ...

    class Sensor:
        def __init__(self, temp: float, pressure: float):
            """
            Создание и подготовка к работе объекта "Сенсор"
            :param temp: Измеренная температура в градусах цельсия
            :param pressure: Измеренное давление в Па

            Примеры:
            >>> sensor1 = Sensor(-30, 101325)  # инициализация экземпляра класса
            """
            if not isinstance(temp, (int, float)):
                raise TypeError("Температура должена быть типа int или float")
            if temp <= -273.15:
                raise ValueError("Температура должна быть выше абсолютного нуля")
            if not isinstance(pressure, (int, float)):
                raise TypeError("Давление должно быть int или float")
            if pressure < 0:
                raise ValueError("Давление не может быть отрицательным числом")
            self.temp = temp
            self.pressure = pressure

        def is_temp_less_than_zero(self) -> bool:
            """
            Функция которая проверяет отрицательная ли температура
            :return: Температура меньше 0
            Примеры:
            >>> sensor2 = Sensor(15, 101010)
            >>> sensor2.is_temp_less_than_zero()
            """
            ...

        def is_vacuum(self) -> bool:
            """
            Функция которая проверяет наличия вакуума
            :return: Зафиксирован вакуум
            Примеры:
            >>> sensor3 = Sensor(7000, 50000)
            >>> sensor3.is_vacuum()
            """
            ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
