from sys import maxsize  # импорт константы возвращающей максимальное число

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # Определяем вид объекта при выводе на консоль
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # Определяем операцию сравнения объектов данного класса (каким образом сравниваем)
    # если ид не определен или ид равны, а так же имена равны. Тогда считаем что группы равны
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # Функция смотрит на налиичие идентификатора. Если он есть то возврашает еего значение иначе возвращает
    # в качестве идентификатора максимальное число
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
