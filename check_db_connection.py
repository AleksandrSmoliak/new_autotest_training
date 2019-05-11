import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group
# Устанавливаем соединение с БД
#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# Выполняем некие действия после коннекта
#try:
    # Создаем курсор дляч чтения данных из БД
#    cursor = connection.cursor()
#    # создаем запрос к БД (делаем выборку всех данных из таблицы group_list
#    cursor.execute("select * from group_list")
#    # делаем цикл и проходим по всем значениям в таблице( метод fetchall возвращает данные в строковом виде)
#    for row in cursor.fetchall():
#        print(row)
#finally:
#    connection.close()

# Для проверки ОРМ
########################################
# Устанавливаем соединение с БД
#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# Выполняем некие действия после коннекта
#try:
    # Создаем курсор дляч чтения данных из БД
#    l = db.get_group_list()
#    for item in l:
#        print(item)
#    print(len(l))
#finally:
#   pass
###########################################
# Устанавливаем соединение с БД
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# Выполняем некие действия после коннекта
#try:
    # Создаем курсор дляч чтения данных из БД
#    l = db.get_contact_list()
#    for item in l:
#        print(item)
#    print(len(l))
#finally:
#   pass

##############################
# Получаем список контактов входящих в переданную в качестве параметра группу
try:
    # Создаем курсор дляч чтения данных из БД
    l = db.get_contacts_in_group(Group(id=309))
    for item in l:
        print(item)
    print(len(l))
finally:
   pass
##############################