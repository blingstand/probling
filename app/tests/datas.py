BIG_EXTRACT = """Bordeaux (prononcé /bɔʁ.do/1 Écouter) est une commune du Sud-Ouest de la France. Capitale de la Gaule aquitaine dès le début du IIIe siècle, puis du duché d'Aquitaine et enfin de l'ancienne province de Guyenne sous l'Ancien régime, elle est aujourd'hui le chef-lieu de la région Nouvelle Aquitaine, préfecture du département de la Gironde et le siège de Bordeaux Métropole."""
SMALL_EXTRACT = """Bergerac est une commune française située dans le département de la Dordogne, en région Nouvelle-Aquitaine."""
QUESTIONS = ["où se trouve le pont Chaban-Delmas ?",#1\
        "Où se trouve le pont Chaban-Delmas ?",\
        "connais-tu le pont Chaban-Delmas ?",\
        "Connais-tu le pont Chaban-Delmas ?",\
        "connaissez-vous le pont Chaban-Delmas ?", #5\
        "Connaissez-vous le pont Chaban-Delmas ?",\
        "connais-tu l'adresse du pont Chaban-Delmas ?",\
        "Connais-tu l'adresse du pont Chaban-Delmas ?",\
        "connaissez-vous l'adresse du pont Chaban-Delmas ?",\
        "Connaissez-vous l'adresse du pont Chaban-Delmas ?", #10\
        "peux-tu me parler du pont Chaban-Delmas ?",\
        "Peux-tu me parler du pont Chaban-Delmas ?",\
        "pouvez-vous me parler du pont Chaban-Delmas ?",\
        "Pouvez-vous me parler du pont Chaban-Delmas ?",\
        "Que peux-tu me dire sur le pont Chaban-Delmas ?",#15\
        "Que peux-tu me dire sur le pont Chaban-Delmas qui se trouve à Bordeaux ?",\
        "Que pouvez-vous me dire sur le pont Chaban-Delmas qui se trouve à Bordeaux ?",\
        "sais-tu quelque chose à propos du pont Chaban-Delmas ?",\
        "Sais-tu quelque chose à propos du pont Chaban-Delmas ?", \
        "savez-vous quelque chose à propos du pont Chaban-Delmas ?",#20\
        "Savez-vous quelque chose à propos du pont Chaban-Delmas ?",\
        "sais-tu quelque chose sur le pont Chaban-Delmas ?",\
        "Sais-tu quelque chose sur le pont Chaban-Delmas ?",\
        "Savez-vous quelque chose sur le pont Chaban-Delmas ?",\
        "savez-vous quelque chose sur le pont Chaban-Delmas ?",#25\
        "as-tu des informations sur le pont Chaban-Delmas ?",\
        "As-tu des informations sur le pont Chaban-Delmas ?",\
        "avez-vous des informations sur le pont Chaban-Delmas ?",
        "Que connais-tu du pont Chaban-Delmas ?",\
        "Avez-vous des informations sur le pont Chaban-Delmas ?",#30\
        "Que connais-tu de la Tour Eiffel ?",\
        "Que connaissez-vous du pont Chaban-Delmas ?",\
        "Est-ce que tu connais le pont Chaban-Delmas ?",\
        "Est-ce que tu connais l'adresse du pont Chaban-Delmas ? ",\
        "Est-ce que vous connaissez le pont Chaban-Delmas ?", #35\
        "Est-ce que vous connaissez l'adresse du pont Chaban-Delmas ? ",\
        "Est-ce que vous connaissez l'adresse d'Openclassroom ? ",\
        "Où se situe le pont Chaban-Delmas ?",\
        "Où est le pont Chaban-Delmas ?"\
        ]




 # -------- test user stories
class test():
    def _get_el(self, selector):
        return self.DRIVER.find_element_by_css_selector(selector)

    def open_page(self):
        self.DRIVER.get("http://127.0.0.1:5000/")
        my_button = self._get_el("button")
        my_input = self._get_el("#myInput")
        return my_input, my_button 

    #10
    def test_presence_input(self):
        #tests the presence of the #myInput element 
        my_input = self.open_page()[0]
        assert my_input is not None

    #11
    def test_presence_button(self):
        #tests the presence of the class .button element 
        my_button = self.open_page()[1]
        assert my_button is not None

    #12
    def test_ask_something(self):
        #test wether the question is displayed
        my_input, my_button = self.open_page()
        start_question = "Où se trouve Bordeaux ?"
        my_input.send_keys(start_question)
        my_button.click()
        self.WAIT.until(lambda driver: self.DRIVER.find_element_by_css_selector(".chatSelf .chat-message").is_displayed())
        
        chat_message = self._get_el(".chatSelf .chat-message")
        text_question = chat_message.text
        assert text_question == start_question

    #13 
    def test_error_message(self):
        my_input, my_button = self.open_page()
        start_question = ""
        my_input.send_keys(start_question)
        my_button.click()
        self.WAIT.until(lambda driver: self.DRIVER.find_element_by_css_selector(".rep-chat-message").is_displayed())
        
        chat_message = self._get_el(".rep-chat-message")
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
        my_input, my_button = self.open_page()
        start_question = "Où se trouve Bordeaux ?"
        my_input.send_keys(start_question)
        my_button.click()
        self.WAIT.until(lambda driver: self.DRIVER.find_element_by_css_selector(".rep-chat-message").is_displayed())
        
        chat_message = self._get_el(".rep-chat-message p:first-child")
        answer1 = chat_message.text
        answer1 = self.first_caracters(answer1, 32)
        chat_message = self._get_el(".rep-chat-message p:nth-child(2)")
        if chat_message is not None:
            answer2 = True
        chat_message = self._get_el(".rep-chat-message p:nth-child(3)")
        answer3 = chat_message.text
        answer3 = self.first_caracters(answer3, 8)
        expected_answer = ["Laisse-moi t'en parler un peu :)", True, "Bordeaux"]
        received_answer = [answer1, answer2, answer3]
        self.DRIVER.quit()
        assert expected_answer == received_answer