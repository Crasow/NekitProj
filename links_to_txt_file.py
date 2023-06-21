import time
from datetime import datetime
import keyboard
import pyperclip
import pyautogui

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


def switch_tab_and_copy_link():
    # switch tab
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.1)
    # select link
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.1)
    # copy link
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(0.3)

def save_staff_to_txt(staff_list):
    with open('links.txt', 'a') as file:
        file.write('-' * 20 + str(datetime.now()) + '-' * 20 + '\n')
        for el in staff_list:
            file.write(el + '\n')


if __name__ == '__main__':
    # debug staff
    # browser = webdriver.Chrome()
    # open_tabs_for_test(browser)

    while True:
        tab_qty = int(
            input(
                "Открой страницу перед теми, которые надо скопировать и введи кол-во стр для копирования "))
        print('нажми на о чтоб начать')
        keyboard.wait('o')

        for el in range(tab_qty):
            switch_tab_and_copy_link()

            links.append(pyperclip.paste())

        save_staff_to_txt(links)

        links.clear()
