import pymysql.cursors


# Устанавливаем соединение с БД
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# Выполняем некие действия после коннекта
try:
    # Создаем курсор дляч чтения данных из БД
    cursor = connection.cursor()
    # создаем запрос к БД (делаем выборку всех данных из таблицы group_list
    cursor.execute("select * from group_list")
    # делаем цикл и проходим по всем значениям в таблице( метод fetchall возвращает данные в строковом виде)
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()