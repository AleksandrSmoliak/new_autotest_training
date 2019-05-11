from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp

class ORMFixture:
    # Объект на основании которого делается привязка
    db = Database()

    # Описание класса для привязки к таблице с группами. Привязка осуществляется на уровне классов. В параметре классов
    # указываем вложенный класс db.Entity для связки класса с нашей БД
    class ORMGroup(db.Entity):
        # Описываем набор свойств и привязываем к полям таблицы. PrimaryKey - обязательное, Optional - не обязательное.
        # в качестве параметра указываем тип данных в полях БД. Параметр column связывает переменную с полем в БД
        # _table_ - тут указываем навание таблицы
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        # Указываем связку с контактами. table - таблица связывающая объекты. column - колонка в которой происходит
        # связка. revese - свойсто которое является парным для данного класса. lazy - извлечние данных по связанным
        # объектам происходит только в момент обращения к сойству.
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    # Описание класса для привязки к таблице с контактами (так же как выше)
    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')
        # Указываем связку с группами. table - таблица связывающая объекты. column - колонка в которой происходит
        # связка. revese - свойсто которое является парным для данного класса.
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    # Осуществляем привязку к БД. conv=decoders - разрешаем конвертировать данны через pymysql
    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        # Сопоставляем свойства классов с полями в таблице БД
        self.db.generate_mapping()
        sql_debug(True)

    # Конвертируем ОРМ объекты в обекты класса
    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    # Реализуем методы которые получают списки объектов. Преобразуем данные в модели наших классов
    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    # Конвертируем ОРМ объекты в обекты класса
    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    # Получаем список контактов которые входят в определенную группу (передаем в метод модельный объект
    @db_session
    def get_contacts_in_group(self, group):
        # Делаем выборку из групп где id группы соответствует id переданного объекта. Преобразуем полученные значения
        # список, для того что бы можно было обратиться по индексу
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        # Конвертивуем полученный список в модельшые объекты класса
        return self.convert_contacts_to_model(orm_group.contacts)

    # Получаем список контактов которые не входят в заданную группу
    @db_session
    def get_contacts_not_in_group(self, group):
        # Делаем выборку из групп где id группы соответствует id переданного объекта. Преобразуем полученные значения
        # список, для того что бы можно было обратиться по индексу
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        # Выбираем список контактов у которых список групп не содержит заданную группу
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
        # Конвертивуем полученный список в модельшые объекты класса
