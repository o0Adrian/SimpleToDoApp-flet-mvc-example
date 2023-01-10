from flet_mvc import FletController, alert
import flet as ft

# Controller
class Controller(FletController):
    
    def add_clicked(self, e=None):
        # NOTE: In order to prevent assigning value, accesing current and then reset value.
        # Flet-MVC next update (v1.0.0) will make things easier and prevent the usage of
        # "self.model.node.current.value" by only calling "self.model.node()" and
        # "self.model.new_task.current.value = ''" by only "calling self.model.node.reset()"
        self.model.task.set_value(self.model.new_task.current.value) 
        if self.model.task() == "":
            self.alert("No task given, please write your to-do task.", alert.WARNING)
        self.model.tasks_view.current.controls.append(ft.Checkbox(label=self.model.task()))
        self.model.new_task.current.value = ""

        self.update()
        self.model.new_task.current.focus()
        self.model.number_of_tasks.reset() 
        
    def on_keyboard(self, e: ft.KeyboardEvent):
        if e.key == "Enter":
            self.add_clicked()
