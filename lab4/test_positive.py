import time

class TestPositive:
    URL = "file:///C:/Users/Серёжа/Desktop/lab4/contact_form.html"
    def test_successful(self, driver):
        from contact_page import ContactPage
        page = ContactPage(driver, self.URL)
        page.open_contact_form()
        
        test_data = {
            "full_name": "Иванов Иван Иванович",
            "email": "ivan@email.com",
            "topic": "technical",
            "message": "Сообщение о проблеме",
            "agreement": True
        }
        page.fill_all(test_data)
        time.sleep(1)
        page.submit_form()
        time.sleep(2)

        assert page.is_element_visible(page.SUCCESS_MESSAGE)