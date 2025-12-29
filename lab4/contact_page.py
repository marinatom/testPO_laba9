from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactPage(BasePage):
    FULL_NAME_INPUT = (By.ID, "fullName")
    EMAIL_INPUT = (By.ID, "email")
    TOPIC_SELECT = (By.ID, "topic")
    MESSAGE_TEXTAREA = (By.ID, "message")
    AGREEMENT_CHECKBOX = (By.ID, "agreement")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    FULL_NAME_ERROR = (By.ID, "fullNameError")
    EMAIL_ERROR = (By.ID, "emailError")
    TOPIC_ERROR = (By.ID, "topicError")
    MESSAGE_ERROR = (By.ID, "messageError")
    AGREEMENT_ERROR = (By.ID, "agreementError")
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    def open_contact_form(self):
        self.driver.get(self.url)  
    
    def enter_full_name(self, full_name):
        element = self.find_element(self.FULL_NAME_INPUT, timeout=10)
        if element:
            element.clear()
            element.send_keys(full_name)
        else:
            print(f"Элемент {self.FULL_NAME_INPUT} не найден!")
    
    def enter_email(self, email):
        element = self.find_element(self.EMAIL_INPUT, timeout=10)
        if element:
            element.clear()
            element.send_keys(email)
        else:
            print(f"Элемент {self.EMAIL_INPUT} не найден!")
    
    def select_topic(self, topic_key):
        element = self.find_element(self.TOPIC_SELECT, timeout=10)
        if element:
            select = Select(element)
            select.select_by_value(topic_key)
        else:
            print(f"Элемент {self.TOPIC_SELECT} не найден!")
    
    def enter_message(self, message):
        element = self.find_element(self.MESSAGE_TEXTAREA, timeout=10)
        if element:
            element.clear()
            if message:
                element.send_keys(message)
        else:
            print(f"Элемент {self.MESSAGE_TEXTAREA} не найден!")
    
    def check_agreement(self):
        element = self.find_element(self.AGREEMENT_CHECKBOX, timeout=10)
        if element and not element.is_selected():
            element.click()
        elif not element:
            print(f"Элемент {self.AGREEMENT_CHECKBOX} не найден!")
    
    def uncheck_agreement(self):
        element = self.find_element(self.AGREEMENT_CHECKBOX, timeout=10)
        if element and element.is_selected():
            element.click()
        elif not element:
            print(f"Элемент {self.AGREEMENT_CHECKBOX} не найден!")
    
    def submit_form(self):
        element = self.find_clickable_element(self.SUBMIT_BUTTON, timeout=10)
        if element:
            element.click()
        else:
            print(f"Элемент {self.SUBMIT_BUTTON} не найден!")
    
    def fill_all(self, data):
        """Заполнить все поля формы"""
        print(f"Заполняем форму данными: {data}")
        self.enter_full_name(data.get("full_name", ""))
        self.enter_email(data.get("email", ""))
        self.select_topic(data.get("topic", "general"))
        self.enter_message(data.get("message", ""))
        
        if data.get("agreement", False):
            self.check_agreement()
        else:
            self.uncheck_agreement()

