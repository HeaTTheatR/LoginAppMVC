import os
from typing import Union, NoReturn

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from Model.base import Base
from View.screens import screens


class LoginAppMVC(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base = Base()
        self.load_all_kv_files()
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager()

    def build(self) -> ScreenManager:
        return self.manager_screens

    def generate_application_screens(self, interval: Union[int, float]) -> NoReturn:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"](self.base)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def on_start(self) -> NoReturn:
        Clock.schedule_once(self.generate_application_screens, 1)

    def load_all_kv_files(self) -> NoReturn:
        for d, dirs, files in os.walk(self.directory):
            for f in files:
                if (
                    os.path.splitext(f)[1] == ".kv"
                    and f != "style.kv"
                    and "Updates" not in d
                    and "__MACOS" not in d
                ):
                    path_to_kv_file = os.path.join(d, f)
                    with open(path_to_kv_file, encoding="utf-8") as kv_file:
                        Builder.load_string(kv_file.read())


LoginAppMVC().run()
