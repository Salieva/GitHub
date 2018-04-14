# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from app_contact import App_contact


@pytest.fixture
def app(request):
    fixture = App_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact(app):
    app.open_page()
    app.trying_lo_login(user = "admin", password =  "secret")
    app.adding_new_contact(Contact(firstname = 'Bill', middlename = 'Bill', lastname ='Imus',\
        nickname ='Billimus', title = 'QA Tester', company ='QA Solutions', address ='Somewhere in the Universe',\
        home_phone ='+122222222', mobile ='+13333333', work_phone = '+14444444', fax ='+15555555',\
        email_1 ='Bill_1@qa.com', email_2 ='Bill_2@qa.com', email_3 ='Bill_2@qa.com', homepage ='IhaveNoPage.com',\
        byear ='2000',ayear='2001', city ='Sim City', phone2 ='+156666666', notes_here ='some notes here'))
    app.log_out()



