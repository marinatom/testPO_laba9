import time

class TestNegative:
    URL = "file:///C:/Users/Серёжа\Desktop\lab4/contact_form.html"
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