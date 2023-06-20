from flet_mvc import FletController, alert
import flet as ft


# Controller
class Controller(FletController):
    def add_clicked(self, e=None):
        self.model.task.set_value(self.model.new_task())
        if self.model.task() == "":
            self.alert("No task given, please write your to-do task.", alert.WARNING)
        self.model.tasks_view.append(ft.Checkbox(label=self.model.task()))
        self.model.new_task.reset()
        self.model.number_of_tasks.reset()
        self.model.new_task.current.focus()

        self.update()

    def on_keyboard(self, e: ft.KeyboardEvent):
        if e.key == "Enter":
            self.add_clicked()
