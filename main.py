import json
import time
from selenium import webdriver
from datetime import datetime
import keyboard

links = []


def open_tabs_for_test(browser):
    browser.get("https://www.example.com")
    browser.execute_script("window.open('https://www.youtube.com')")
    browser.execute_script("window.open('https://www.openai.com')")
    browser.execute_script(
        "window.open('https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab')")
    browser.execute_script("window.open('https://www.youtube.com/watch?v=tViDT_gEpDk')")
    browser.execute_script("window.open('https://github.com/UB-Mannheim/tesseract/wiki')")
    browser.execute_script(
        "window.open('https://stackoverflow.com/questions/5217519/what-does-opencvs-cvwaitkey-function-do')")
    browser.execute_script("window.open('https://pypi.org/project/selenium/')")
    browser.execute_script("window.open('https://github.com/mozilla/geckodriver/releases')")


def switch_tab():
    keyboard.press('ctrl')
    keyboard.press('tab')
    time.sleep(0.1)
    keyboard.release('tab')
    keyboard.release('ctrl')


def save_path_to_json(browser_path):
    data = {
        'browser_path': browser_path
    }
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)


def get_path_from_json():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        return data['browser_path']


if __name__ == '__main__':
    browser = webdriver.Chrome()

    open_tabs_for_test(browser)

    while True:
        tab_qty = int(
            input("Открой первую из страниц для копирования и введи сколько всего надо скопировать(включая эту) "))
        print('нажми на о чтоб начать')
        keyboard.wait('o')

        for el in range(tab_qty):
            current_url = browser.current_url
            links.append(browser.current_url)

            switch_tab()

        with open('tvoi_links_suka.txt', 'a') as file:
            file.write('-' * 20 + str(datetime.now()) + '-' * 20 + '\n')
            for link in links:
                file.write(link + '\n')

        links.clear()
