import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://telemost.yandex.ru/"
MEETING_URL = "https://telemost.yandex.ru/j/23824620345487"
MEETING_CODE = "2382 4620 3454 87"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    prefs = {
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.notifications": 2,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()



def test_join_by_code(driver):
    driver.get(BASE_URL)
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(., 'Подключиться')]").click()
    time.sleep(2)

    code_input = driver.find_element(By.XPATH, "//input")
    code_input.send_keys(MEETING_CODE)

    driver.find_element(By.XPATH, "//button[contains(., 'Подключиться')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(., 'Продолжить в браузере')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(., 'Подключ')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(., 'Подключ')]").click()
    assert "telemost" in driver.current_url


def test_join_meeting(driver):
    driver.get(MEETING_URL)
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(., 'Продолжить в браузере')]").click()
    time.sleep(2)

    name_inputs = driver.find_elements(By.XPATH, "//input")
    if name_inputs:
        name_inputs[0].send_keys("Test User")

    driver.find_element(By.XPATH, "//button[contains(., 'Подключ')]").click()
    time.sleep(5)

    assert "telemost" in driver.current_url


def test_support_page_redirect(driver):
    wait = WebDriverWait(driver, 15)

    driver.get(BASE_URL)

    support_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(., 'Поддержка')] | "
                "//button[contains(., 'Поддержка')]"
            )
        )
    )

    support_button.click()

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    wait.until(
        lambda d: "yandex.ru/support" in d.current_url
    )

    assert driver.current_url.startswith(
        "https://yandex.ru/support/yandex-360/customers/telemost/web/ru/"
    )



def test_invalid_link(driver):
    driver.get("https://telemost.yandex.ru/j/invalid_link_123")
    time.sleep(3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()

    assert (
        "не существует" in body_text
        or "ошибка" in body_text
    )


def test_screen_share(driver):
    wait = WebDriverWait(driver, 15)

    driver.get(MEETING_URL)
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(., 'Продолжить в браузере')]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(., 'Подключ')]").click()
    time.sleep(5)

    share_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Демонстра')]")
        )
    )

    share_button.click()
    time.sleep(5)

    stop_buttons = driver.find_elements(
        By.XPATH,
        "//*[contains(., 'Остановить')]"
    )

    assert len(stop_buttons) > 0