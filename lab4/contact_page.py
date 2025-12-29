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
        self.open()
    
    def enter_full_name(self, full_name):
        element = self.find_clickable_element(self.FULL_NAME_INPUT)
        element.clear()
        element.send_keys(full_name)
    
    def enter_email(self, email):
        element = self.find_clickable_element(self.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)
    
    def select_topic(self, topic_key):
        element = self.find_clickable_element(self.TOPIC_SELECT)
        select = Select(element)
        select.select_by_value(topic_key)
    
    def enter_message(self, message):
        element = self.find_clickable_element(self.MESSAGE_TEXTAREA)
        element.clear()
        if message:
            element.send_keys(message)
    
    def check_agreement(self):
        element = self.find_clickable_element(self.AGREEMENT_CHECKBOX)
        if not element.is_selected():
            element.click()
    
    def uncheck_agreement(self):
        element = self.find_clickable_element(self.AGREEMENT_CHECKBOX)
        if element.is_selected():
            element.click()
    
    def submit_form(self):
        element = self.find_clickable_element(self.SUBMIT_BUTTON)
        element.click()
    
    def fill_all(self, data):
        self.enter_full_name(data.get("full_name", ""))
        self.enter_email(data.get("email", ""))
        self.select_topic(data.get("topic", "general"))
        self.enter_message(data.get("message", ""))
        
        if data.get("agreement", False):
            self.check_agreement()
        else:
            self.uncheck_agreement()