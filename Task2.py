"""2) Реализовать класс Road (дорога), в котором определить атрибуты: length
(длина), width (ширина). Значения данных атрибутов должны передаваться при
создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
метода."""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, depth):
        mass = 25
        result = self._length * self._width * mass * depth / 1000
        print(f"Для покрытия полотна потребуеся {result} тонн асфальта")


asphalt = Road(20, 5000)
asphalt.mass_of_asphalt(5)
