from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def create_driver(profile_path: str):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={profile_path}")

    options.add_argument("--mute-audio")
    options.add_argument("--disable-web-security")

    return webdriver.Chrome(options=options)


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


def make_lesson(driver: webdriver.Chrome, lesson_url: str, tabs: int):
    print(f"Starting {tabs} tabs")

    for i in range(0, tabs):
        driver.execute_script(f"window.open('{lesson_url}')")
        sleep(2)

    print("All tabs opened\nStarting lessons")

    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    current_tab = 0

    tabs_finished = set()

    try:
        while True:
            if len(tabs_finished) == tabs:
                break

            current_tab += 1
            if current_tab == tabs:
                current_tab = 0

            driver.switch_to.window(driver.window_handles[current_tab])

            if current_tab in tabs_finished:
                continue

            if is_challenge_step(driver):
                sleep(5)
                make_challenge_step(driver)
                sleep(1)
                press_enter(driver)
                tabs_finished.add(current_tab)
                print(f"Tab {current_tab} finished")
                continue

            click_all_buttons(driver)
            press_enter(driver)

        for i in range(0, tabs):
            driver.switch_to.window(driver.window_handles[i])
            click_all_buttons(driver)
            sleep(2)
            driver.close()

        print("All tabs finished")

    except Exception as e:
        print(e)
        print("An error occurred, finishing tabs")
        sleep(100)
