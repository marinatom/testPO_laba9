import time

class TestPositive:
    URL = "file://" + __file__.replace("test_positive.py", "contact_form.html")
    
    def test_successful(self, driver):
        # Отладочный код
        print(f"Открываем URL: {self.URL}")
        driver.get(self.URL)
        time.sleep(2)  # Ждем загрузки
        
        # Проверяем, что страница загрузилась
        print(f"Текущий URL: {driver.current_url}")
        print(f"Заголовок страницы: {driver.title}")
        print(f"Содержимое страницы (первые 500 символов): {driver.page_source[:500]}")
        
        from contact_page import ContactPage
        page = ContactPage(driver, self.URL)

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
