import flet as ft
from flet_mvc import data, FletModel


# Model
class Model(FletModel):
    @data
    def tasks_view(self):
        return []

    @data
    def new_task(self):
        return ""

    @data
    def task(self):
        return ""

    @data
    def number_of_tasks(self):
        return f"Total tasks: {len(self.tasks_view())}"
