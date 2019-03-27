from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company_name=None,
                 company_address=None, home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None, sec_phone = None,
                 email=None, email2=None, email3=None, homepage=None, birthday_selected=None, birthmont_selected=None,
                 byear=None, home_address=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company_name = company_name
        self.company_address = company_address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.sec_phone = sec_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_selected = birthday_selected
        self.birthmont_selected = birthmont_selected
        self.byear = byear
        self.home_address = home_address

    # Функция для обозначения представления контактов в консоли при отладке и ошибках
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    # Функция определяющая принцип сравнения объектов данного класса
    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and (self.lastname == other.lastname or self.lastname is None or other.lastname is None) and \
               (self.firstname == other.firstname or self.firstname is None or other.firstname is None)

    # Подставляем максимальное значение если ид не опеределен, иначе возвращаем знавчение полученного ид
    # (функция) используется как ключ для сортировки списка
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize