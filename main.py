from utils import create_driver, make_lesson
from dotenv import load_dotenv
from os import getenv


# loading the environment variables
load_dotenv()
LESSON_URL = getenv("LESSON_URL")
PROFILE_PATH = getenv("PROFILE_PATH")

print(f"Lesson URL: {LESSON_URL}")
print(f"Profile Path: {PROFILE_PATH}")

# creating the web driver
driver = create_driver(PROFILE_PATH)

# making the lesson
make_lesson(driver, LESSON_URL, 30)

print("Lesson finished")

# closing the web driver
driver.quit()
