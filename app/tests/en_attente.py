
from selenium import webdriver
import selenium.webdriver.support.ui as ui

self.DRIVER = webdriver.Firefox()
def get_el(selector):
    """ select an element"""
    return self.DRIVER.find_element_by_css_selector(selector)

def open_page():
    """ open a page and return an input and a button"""
    self.DRIVER.get("http://127.0.0.1:5000/")
    my_button = get_el("button")
    my_input = get_el("#myInput")
    return my_input, my_button 

class TestUserStories():
    """ Class that gathers all the tests"""
    WAIT = ui.WebDriverWait(self.DRIVER, 1000)

# -------- test user stories
    #10
    def test_presence_input(self):
        #tests the presence of the #myInput element 
        my_input = open_page()[0]
        assert my_input is not None

    #11
    def test_presence_button(self):
        #tests the presence of the class .button element 
        my_button = open_page()[1]
        assert my_button is not None

    #12
    def test_ask_something(self):
        #test wether the question is displayed
        my_input, my_button = open_page()
        start_question = "Où se trouve Bordeaux ?"
        my_input.send_keys(start_question)
        my_button.click()
        self.WAIT.until(lambda driver: self.DRIVER.find_element_by_css_selector(".chatSelf .chat-message").is_displayed())
        
        chat_message = get_el(".chatSelf .chat-message")
        text_question = chat_message.text
        assert text_question == start_question

    #13 
    def test_error_message(self):
        my_input, my_button = open_page()
        start_question = ""
        my_input.send_keys(start_question)
        my_button.click()
        self.WAIT.until(lambda driver: self.DRIVER.find_element_by_css_selector(".rep-chat-message").is_displayed())
        
        chat_message = get_el(".rep-chat-message")
        response_text = chat_message.text
        assert response_text == "Désolé je ne connais pas cet endroit ... Peut-être pourrais-tu reformuler ou me poser une autre question ?"

    def first_caracters(self, text, size):
        to_return = ""
        for carac in text:
            to_return += carac
            if len(to_return) == size:
                return to_return
    #14 
    def test_get_response_first_part(self):
        my_input, my_button = open_page()
        start_question = "Où se trouve Bordeaux ?"
        my_input.send_keys(start_question)
        my_button.click()
        self.WAIT.until(lambda driver: self.DRIVER.find_element_by_css_selector(".rep-chat-message").is_displayed())
        
        chat_message = get_el(".rep-chat-message p:first-child")
        answer1 = chat_message.text
        answer1 = self.first_caracters(answer1, 32)
        chat_message = get_el(".rep-chat-message p:nth-child(2)")
        if chat_message is not None:
            answer2 = True
        chat_message = get_el(".rep-chat-message p:nth-child(3)")
        answer3 = chat_message.text
        answer3 = self.first_caracters(answer3, 8)
        expected_answer = ["Laisse-moi t'en parler un peu :)", True, "Bordeaux"]
        received_answer = [answer1, answer2, answer3]
        self.DRIVER.quit()
        assert expected_answer == received_answer