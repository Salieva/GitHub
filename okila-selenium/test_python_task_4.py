# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_python_lesson_1_task_1(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="ccc", header="ccc", footer="ccc"))
    app.return_to_group_page()
    app.logout()


def test_python_lesson_empty_1_task_1(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="", footer=""))
    app.return_to_group_page()
    app.logout()

