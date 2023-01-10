import flet as ft
from flet_mvc import data


# Model
class Model():
    def __init__(self):
        self.new_task = ft.Ref[ft.TextField]()
        self.tasks_view = ft.Ref[ft.Column]()
    
    @data
    def task(self):
        return ""
    
    # This will be available when flet-mvc v1.0 get's deployed
    
    # @data
    # def number_of_tasks(self):
    #     return f"Total tasks: {self.total_tasks()}"
    
    # def total_tasks(self):
    #     return len(self.tasks_view.current.controls)