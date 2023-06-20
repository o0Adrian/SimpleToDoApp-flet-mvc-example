from flet_mvc import FletView
import flet as ft


# view
class MainView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Column(
                width=600,
                controls=[
                    ft.Row(
                        controls=[
                            ft.TextField(
                                ref=model.new_task,
                                hint_text="What needs to be done?",
                                expand=True,
                            ),
                            ft.FloatingActionButton(
                                icon=ft.icons.ADD, on_click=controller.add_clicked
                            ),
                        ]
                    ),
                    ft.Column(ref=model.tasks_view),
                    ft.Row(
                        controls=[
                            ft.Text(ref=model.number_of_tasks, expand=True),
                        ]
                    ),
                ],
            )
        ]
        super().__init__(model, view, controller)
