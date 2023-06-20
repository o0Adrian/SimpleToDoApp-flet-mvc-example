from mvc.controller import Controller
from mvc.view import MainView
from mvc.model import Model

import flet as ft


def main(page):
    # MVC set-up
    model = Model()
    controller = Controller(page, model)
    model.controller = controller
    view = MainView(controller, model)

    # Settings
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_keyboard_event = controller.on_keyboard
    page.theme_mode = "light"

    # Run
    page.add(*view.content)


ft.app(target=main)
