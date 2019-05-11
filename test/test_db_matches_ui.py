from model.group import Group


# Тест для проверки того, что данные полученные из БД и инерфейса равны.
def test_group_list(app, db):
    # Загружаем сприсок из приложения
    ui_list = app.group.get_group_list()

    def clean(group):
        # Очищаем от пробелов поле name. Ф-я strip очищает от пробелов в начале и в конце
        return Group(id=group.id, name=group.name.strip())
    # Загружаем список из БД. Очищаем список от лишних пробелов
    db_list = map(clean, db.get_group_list())
    # Сравниваем списки предварительно сортируя списки по максимальному ИД
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)