import json
import time
import json
import time
from selenium import webdriver
from datetime import datetime
import keyboard
from selenium import webdriver
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from collections import deque


def copy_recent_links():
    # Get all window handles

    initial_handle = driver.current_window_handle

    window_handles = driver.window_handles

    # Remove the initial window handle
    window_handles.remove(initial_handle)

    # Get the last three tab handles
    recent_tabs = deque(window_handles, maxlen=3)

    # Iterate over the last three tabs and copy the links
    copied_links = []
    for handle in recent_tabs:
        driver.switch_to.window(handle)
        WebDriverWait(driver, 10).until(lambda driver: driver.current_url != "about:blank")

        # Get the current URL
        current_url = driver.current_url
        copied_links.append(current_url)

    # Print the copied links
    for link in copied_links:
        print(link)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get("https://www.example.com")
    driver.execute_script("window.open('https://www.youtube.com')")
    driver.execute_script("window.open('https://www.openai.com')")
    driver.execute_script(
        "window.open('https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab')")
    driver.execute_script("window.open('https://www.youtube.com/watch?v=tViDT_gEpDk')")
    driver.execute_script("window.open('https://github.com/UB-Mannheim/tesseract/wiki')")
    driver.execute_script(
        "window.open('https://stackoverflow.com/questions/5217519/what-does-opencvs-cvwaitkey-function-do')")
    driver.execute_script("window.open('https://pypi.org/project/selenium/')")
    driver.execute_script("window.open('https://github.com/mozilla/geckodriver/releases')")

    while True:
        keyboard.wait('o')

        # Call the function to copy the three most recent links from browser tabs
        copy_recent_links()
