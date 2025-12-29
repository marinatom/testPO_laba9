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
    chrome_options.add_argument("--headless")  # Без графического интерфейса
    chrome_options.add_argument("--no-sandbox")  # Требуется в CI среде
    chrome_options.add_argument("--disable-dev-shm-usage")  # Требуется в CI
    
    # Дополнительные настройки для стабильности:
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")  # Для headless режима
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    
    # Автоматическая установка правильной версии ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    # Создаем драйвер
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  # Неявное ожидание
    
    yield driver
    
    # Закрываем драйвер после теста
    driver.quit()

@pytest.fixture
def contact_form_url():
    """Фикстура для получения URL тестовой формы в GitHub Actions"""
    # В GitHub Actions используем относительный путь
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return f"file://{current_dir}/contact_form.html"
