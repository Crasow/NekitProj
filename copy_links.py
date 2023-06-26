import time
import keyboard
import pyperclip
import logging
from selenium import webdriver
from json_funcs import *


from kb_layout_detector import lang_fix

log_level = logging.DEBUG
data = get_data()
DELAY = data['delay']


def open_tabs_for_test(browser):
    browser.get("https://www.example.com")
    browser.execute_script("window.open('https://www.youtube.com')")
    browser.execute_script("window.open('https://www.openai.com')")
    browser.execute_script(
        "window.open('https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html"
        "#ga397ae87e1288a81d2363b61574eb8cab')")
    browser.execute_script("window.open('https://www.youtube.com/watch?v=tViDT_gEpDk')")
    browser.execute_script("window.open('https://github.com/UB-Mannheim/tesseract/wiki')")
    browser.execute_script(
        "window.open('https://stackoverflow.com/questions/5217519/what-does-opencvs-cvwaitkey-function-do')")
    browser.execute_script("window.open('https://pypi.org/project/selenium/')")
    browser.execute_script("window.open('https://github.com/mozilla/geckodriver/releases')")
    browser.execute_script("window.open('https://rozetka.com.ua/341623342/p341623342/')")
    browser.execute_script("window.open('https://mangapoisk.org/manga/berserk/chapter/9-53')")


def switch_tab():
    keyboard.press('ctrl')
    keyboard.press('tab')
    keyboard.release('tab')
    keyboard.release('ctrl')
    time.sleep(DELAY)


def select_link():
    keyboard.press('ctrl')
    keyboard.press(fixed_signs[0])
    keyboard.release(fixed_signs[0])
    keyboard.release('ctrl')
    time.sleep(DELAY)


def copy():
    keyboard.press('ctrl')
    keyboard.press(fixed_signs[1])
    keyboard.release(fixed_signs[1])
    keyboard.release('ctrl')
    time.sleep(DELAY)


def save_staff_to_txt(staff_list):
    with open('links.txt', 'a', encoding="UTF-8") as file:
        for ell in staff_list:
            file.write(ell + '\n')


def create_logger(logging_level):
    logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()


def main(steps):
    for el in range(steps):
        switch_tab()
        select_link()
        copy()

        logger.debug(f'{pyperclip.paste()} copied')

        links.append(pyperclip.paste())

    save_staff_to_txt(set(links))

    print(f'Скрипт закончил работу. Сохранено {len(set(links))}')

    links.clear()



if __name__ == '__main__':
    # debug staff
    if log_level == logging.DEBUG:
        browser = webdriver.Chrome()
        open_tabs_for_test(browser)

    logger = create_logger(log_level)
    links = []
    fixed_signs = lang_fix()

    logger.debug(fixed_signs)

    if fixed_signs == 'unknown_language':
        logger.critical('Открой скрипт только с англ или ру расскладкой на клаве')
        keyboard.wait()

    tab_qty = int(input("Введи кол-во страниц для копирования: "))
    keyboard.add_hotkey("o", lambda: main(tab_qty))
    print('Нажми на о чтоб начать')

    while True:
        tab_qty = int(input())
