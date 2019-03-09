def test_delete_first_group(app):
    # Удаление новой группы
    app.group.delete_first_group()
    app.session.return_home_page()