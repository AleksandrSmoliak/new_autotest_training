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
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
