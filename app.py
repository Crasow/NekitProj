import tkinter

from customtkinter import *

import copy_links
from json_funcs import *

set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(CTk):
    def __init__(self):
        super().__init__()

        data = get_data()
        self.delay = data['delay']

        self.macro_1 = data['macro_1']
        self.macro_2 = data['macro_2']
        self.macro_3 = data['macro_3']
        self.tab_qty = data['tab_qty']

        self.title("Links getter")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), minsize=10)

        # buttons row 0
        self.macro1_btn = CTkButton(self, fg_color="transparent", border_width=2, command=self.button_redirect('macro1_btn'),
                                    text="Открыть буки", text_color=("gray10", "#DCE4EE"))
        self.macro1_btn.grid(row=0, column=0, padx=20, pady=(10,50), sticky='s')

        self.macro2_btn = CTkButton(self, fg_color="transparent", border_width=2, command=self.button_redirect('macro2_btn'),
                                    text="Прочесть", text_color=("gray10", "#DCE4EE"))
        self.macro2_btn.grid(row=0, column=1, padx=20, pady=10)

        self.macro3_btn = CTkButton(self, fg_color="transparent", border_width=2, command=self.button_redirect('macro2_btn'),
                                    text="Ответить", text_color=("gray10", "#DCE4EE"))
        self.macro3_btn.grid(row=0, column=2, padx=20, pady=10)

        self.copy_links_button = CTkButton(self, fg_color="transparent", border_width=2, command=self.button_redirect('copy_links_button'),
                                           text="Скопировать ссылки", text_color=("gray10", "#DCE4EE"))
        self.copy_links_button.grid(row=0, column=3, padx=20, pady=10)

        # label and entry row 1 and 2
        self.macro_1_text = StringVar()
        self.macro_label_1 = CTkLabel(self, text=f"Кнопка макроса")
        self.macro_label_1.grid(row=1, column=0, padx=20, pady=1, sticky='s')
        self.macro_input_1 = CTkEntry(self, placeholder_text="кнопка макроса", textvariable=self.macro_1_text)
        self.macro_input_1.grid(row=2, column=0, padx=20, pady=1, sticky='n')
        self.macro_input_1.insert(0, self.macro_1) if self.macro_1 else False

        self.macro_2_text = StringVar()
        self.macro_label_2 = CTkLabel(self, text=f"Кнопка макроса", )
        self.macro_label_2.grid(row=1, column=1, padx=20, pady=1, sticky='s')
        self.macro_input_2 = CTkEntry(self, placeholder_text="кнопка макроса", textvariable=self.macro_2_text)
        self.macro_input_2.grid(row=2, column=1, padx=20, pady=1, sticky='n')
        self.macro_input_2.insert(0, self.macro_2) if self.macro_2 else False

        self.macro_3_text = StringVar()
        self.macro_label_3 = CTkLabel(self, text=f"Кнопка макроса")
        self.macro_label_3.grid(row=1, column=2, padx=20, pady=1, sticky='s')
        self.macro_input_3 = CTkEntry(self, placeholder_text="кнопка макроса", textvariable=self.macro_3_text)
        self.macro_input_3.grid(row=2, column=2, padx=20, pady=1, sticky='n')
        self.macro_input_3.insert(0, self.macro_3) if self.macro_3 else False

        self.tab_qty_text = StringVar()
        self.tab_qty_label = CTkLabel(self, text=f"Кол-во страниц для копирования")
        self.tab_qty_label.grid(row=1, column=3, padx=20, pady=1, sticky='s')
        self.tab_qty_entry = CTkEntry(self, placeholder_text="кол-во страниц для копирования",
                                      textvariable=self.tab_qty_text)
        self.tab_qty_entry.grid(row=2, column=3, padx=20, pady=1, sticky='new')
        self.tab_qty_entry.insert(0, self.tab_qty) if self.tab_qty else False

        # text bindings
        self.macro_1_text.trace("w",
                                lambda name, index, mode, text_var=self.macro_1_text: self.on_text_changed(name,
                                                                                                           text_var))
        self.macro_2_text.trace("w",
                                lambda name, index, mode, text_var=self.macro_2_text: self.on_text_changed(name,
                                                                                                           text_var))
        self.macro_3_text.trace("w",
                                lambda name, index, mode, text_var=self.macro_3_text: self.on_text_changed(name,
                                                                                                           text_var))
        self.tab_qty_text.trace("w",
                                lambda name, index, mode, text_var=self.tab_qty_text: self.on_text_changed(name,
                                                                                                           text_var))

    # methods
    def button_redirect(self, button_name):
        if button_name == "macro1_btn":
            print("Button 1 clicked!")
        elif button_name == "macro2_btn":
            print("Button 2 clicked!")
        elif button_name == "macro2_btn":
            print("Button 3 clicked!")
        elif button_name == "copy_links_button":
            copy_links.main()

    def on_text_changed(self, name, text_var):
        var_to_data = {
            "PY_VAR0": "macro_1",
            "PY_VAR1": "macro_2",
            "PY_VAR2": "macro_3",
            "PY_VAR3": "tab_qty"
        }

        new_text = text_var.get()
        data_key = var_to_data.get(name)
        if data_key is not None:
            change_data(data_key, new_text)
            print(f"Text changed in {name}: {new_text}")


if __name__ == '__main__':
    app = App()
    app.mainloop()
