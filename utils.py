from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SLEEP_TIME = 1


def create_driver(profile_path: str):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={profile_path}")

    options.add_argument("--mute-audio")
    options.add_argument("--disable-web-security")

    return webdriver.Chrome(options=options)


def check_if_logged_in(driver: webdriver.Chrome) -> bool:
    all_a_tags = driver.find_elements(by=By.TAG_NAME, value="a")

    for a_tag in all_a_tags:
        if a_tag.get_attribute("data-test") == "profile-tab":
            return True

    return False


def get_username_logged_in(driver: webdriver.Chrome) -> str:
    if not check_if_logged_in(driver):
        return "User not logged in"

    all_a_tags = driver.find_elements(by=By.TAG_NAME, value="a")

    for a_tag in all_a_tags:
        if a_tag.get_attribute("data-test") == "profile-tab":
            return a_tag.get_attribute("href").split("/")[-1]

    return "User not logged in"


def login_on_account(driver: webdriver.Chrome):
    try:
        driver.get("https://www.duolingo.com/learn")

        while not check_if_logged_in(driver):
            sleep(2)
    except Exception as e:
        print(e)


def press_enter(driver: webdriver.Chrome):
    driver.switch_to.active_element.send_keys(Keys.ENTER)


def get_all_buttons(driver: webdriver.Chrome):
    buttons = driver.find_elements(by=By.TAG_NAME, value="button")
    return buttons


def is_challenge_step(driver: webdriver.Chrome):
    buttons = get_all_buttons(driver)

    return len(buttons) >= 10


def check_if_button_is_disabled(button: webdriver.Chrome):
    return button.get_attribute("aria-disabled") == "true"


def click_on_button(driver: webdriver.Chrome, button: webdriver.Chrome):
    if check_if_button_is_disabled(button):
        return
    try:
        button.click()
    except Exception:
        pass


def click_all_buttons(driver: webdriver.Chrome):
    buttons = get_all_buttons(driver)

    for button in buttons:
        click_on_button(driver, button)


def check_if_lesson_is_finished(driver: webdriver.Chrome):
    buttons = get_all_buttons(driver)

    for button in buttons:
        if button.get_attribute("data-test") == "stories-player-done":
            return True
    return False


def make_challenge_step(driver: webdriver.Chrome):
    buttons = get_all_buttons(driver)

    for i in range(0, 5):
        for j in range(5, 10):
            try:
                click_on_button(driver, buttons[i])
                click_on_button(driver, buttons[j])
            except Exception:
                pass


def get_clickable_buttons(driver: webdriver.Chrome):
    buttons = get_all_buttons(driver)

    clickable_buttons = []

    for button in buttons:
        if not check_if_button_is_disabled(button):
            clickable_buttons.append(button)

    return clickable_buttons


def finish_lesson(driver: webdriver.Chrome):
    sleep(SLEEP_TIME)
    click_all_buttons(driver)
    sleep(SLEEP_TIME)
    press_enter(driver)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def get_random_lesson(lesson_urls: list) -> str:
    number_of_lessons = len(lesson_urls)
    random_lesson = lesson_urls[randint(0, number_of_lessons - 1)]
    return random_lesson


def start_new_lesson(driver: webdriver.Chrome, lesson_urls: str):
    lesson_url = get_random_lesson(lesson_urls)
    driver.execute_script(f"window.open('{lesson_url}')")
    sleep(SLEEP_TIME)


def make_lesson(
    driver: webdriver.Chrome,
    lesson_urls: list,
    tabs: int,
    sleep_time: float,
):
    global SLEEP_TIME
    SLEEP_TIME = sleep_time

    print(f"Starting {tabs} tabs")

    current_tab = 0

    try:
        while True:

            while len(driver.window_handles) <= tabs:
                start_new_lesson(driver, lesson_urls)

            current_tab += 1

            if current_tab == tabs + 1:
                current_tab = 1

            driver.switch_to.window(driver.window_handles[current_tab])

            if is_challenge_step(driver):
                sleep(SLEEP_TIME)
                make_challenge_step(driver)
                sleep(SLEEP_TIME)
                finish_lesson(driver)
                continue

            click_all_buttons(driver)
            press_enter(driver)

    except Exception as e:
        print(e)
        print("An error occurred, finishing tabs")
        sleep(100)
