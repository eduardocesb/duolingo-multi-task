import json
from utils import (
    create_driver,
    make_lesson,
    login_on_account,
    get_username_logged_in,
)
from dotenv import load_dotenv
from os import getenv


# loading the environment variables
load_dotenv()
LESSON_URLS = json.loads(getenv("LESSON_URLS"))
PROFILE_PATH = getenv("PROFILE_PATH")
SLEEP_TIME = float(getenv("SLEEP_TIME"))
NUMBER_OF_TABS = int(getenv("NUMBER_OF_TABS"))

# creating the web driver
driver = create_driver(PROFILE_PATH)

login_on_account(driver)

username = get_username_logged_in(driver)

print(f"Logged in as: {username}")
wait = input("Press enter to continue")

# making the lesson
make_lesson(driver, LESSON_URLS, tabs=NUMBER_OF_TABS, sleep_time=SLEEP_TIME)

print("Lesson finished")

# closing the web driver
driver.quit()
