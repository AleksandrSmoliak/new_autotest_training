from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    # Проверяем наличие групп. Если их нет, то создаем.
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # Получаем старый список групп из БД
    old_groups = db.get_group_list()
    # Получаем случайную группу из списка групп
    group = random.choice(old_groups)
    # Удаление новой группы по ИД
    app.group.delete_group_by_id(group.id)
    # Получаем новый список групп из БД
    new_groups = db.get_group_list()
    # Проверяем что произошло удаление новой группы сравнивая их длину
    assert len(old_groups) - 1 == len(new_groups)
    # Удаляем выбранный ранее элемент из списка групп
    old_groups.remove(group)
    # Проверяем получившиеся списки групп
    assert old_groups == new_groups
    # Делаем проверку ниже если выставлен флаг check_ui
    if check_ui:
        # Сравниваем новые списки групп из приложения и БД
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    # Возврат на страницу со списком групп
    app.session.return_home_page()
