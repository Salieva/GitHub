# -*- coding: utf-8 -*-
# test_python_task_4a
import pytest
from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.adding_new_contact(Contact(firstname = 'Bill', middlename = 'Bill', lastname ='Imus',\
        nickname ='Billimus', title = 'QA Tester', company ='QA Solutions', address ='Somewhere in the Universe',\
        home_phone ='+122222222', mobile ='+13333333', work_phone = '+14444444', fax ='+15555555',\
        email_1 ='Bill_1@qa.com', email_2 ='Bill_2@qa.com', email_3 ='Bill_2@qa.com', homepage ='IhaveNoPage.com',\
        byear ='2000',ayear='2001', city ='Sim City', phone2 ='+156666666', notes_here ='some notes here'))
    app.logout()



