#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
	Before to throw Pytest please run the app 
"""
from selenium import webdriver
import selenium.webdriver.support.ui as ui


class testClientSide():


	def setUp(self):
		self.driver = webdriver.Firefox()
		self.wait = ui.WebDriverWait(self.driver, 1000)


	def tearDown(self):
		self.driver.quit()

	def get_el(self, selector):
		return self.driver.find_element_by_css_selector(selector)

	def test_presence_input(self):
		#tests the presence of the #myInput element 
		self.my_input = get_el("#myInput")
		assert self.my_input is not None

	def test_presence_button(self):
		#tests the presence of the class .button element 
		self.button = get_el(".button")
		assert self.button is not None

	def ask_something(self):
		self.my_input.send_keys('connais-tu Bordeaux ?')
		self.my_button = get_el(".button")
		self.wait.until(lambda driver: self.driver.get_el(".SELF-photo").is_displayed())
		self.question = get_el("div.Self-chat p.chat-message")
		assert self.question is not None

