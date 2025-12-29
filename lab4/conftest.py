import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера браузера в CI/CD"""
    
    # Настройки Chrome для CI/CD среды
    chrome_options = Options()
    
    # ОБЯЗАТЕЛЬНЫЕ настройки для GitHub Actions:
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Дополнительные настройки:
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    
    # Автоматическая установка ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    # Создаем драйвер
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # Закрываем драйвер
    driver.quit()

# УДАЛИТЕ эту фикстуру или закомментируйте, если не используется
# @pytest.fixture
# def contact_form_url():
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     return f"file://{current_dir}/contact_form.html"
