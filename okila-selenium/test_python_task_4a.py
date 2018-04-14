# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from contact import Contact
from app_contact import App_contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_contact(unittest.TestCase):
    def setUp(self):
        self.app = App_contact()

    def test_contact(self):
        self.app.open_page()
        self.app.trying_lo_login(user = "admin", password =  "secret")
        self.app.adding_new_contact(Contact(firstname = 'Bill', middlename = 'Bill', lastname ='Imus',\
            nickname ='Billimus', title = 'QA Tester', company ='QA Solutions', address ='Somewhere in the Universe',\
            home_phone ='+122222222', mobile ='+13333333', work_phone = '+14444444', fax ='+15555555',\
            email_1 ='Bill_1@qa.com', email_2 ='Bill_2@qa.com', email_3 ='Bill_2@qa.com', homepage ='IhaveNoPage.com',\
            byear ='2000',ayear='2001', city ='Sim City', phone2 ='+156666666', notes_here ='some notes here'))

        self.app.log_out()


    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
