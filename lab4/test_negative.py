import time
import os

class TestNegative:
    URL = "file://" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "contact_form.html")
    
    def test_empty(self, driver):
        from contact_page import ContactPage
        
        page = ContactPage(driver, self.URL)
        page.open_contact_form()
        
        test_data = {
            "full_name": "Иванов Иван Иванович",
            "email": "",
            "topic": "general",
            "message": "",
            "agreement": True
        }
        
        page.fill_all(test_data)
        time.sleep(0.5)
        page.submit_form()
        time.sleep(1)
        
        assert page.is_element_visible(page.EMAIL_ERROR)
        assert not page.is_element_visible(page.SUCCESS_MESSAGE)
