# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from group import Group
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class python_lesson_1_task_1(unittest.TestCase):
    def setUp(self):
        self.app = Application()


    def test_python_lesson_1_task_1(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_groups_page()
        self.app.create_group(Group(name="ccc", header="ccc", footer="ccc"))
        self.app.return_to_group_page()
        self.app.logout()


    def test_python_lesson_empty_1_task_1(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_groups_page()
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.return_to_group_page()
        self.app.logout()




    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
