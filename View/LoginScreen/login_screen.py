from typing import NoReturn

from kivy.properties import ObjectProperty

from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

from Utility.observer import Observer


class LoginScreenView(MDScreen, Observer):
    """
    A class that implements a visual representation of the model data
    :class:`~Model.login_screen.LoginScreenModel`.

    Implements the login start screen in the user application.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.login_screen.LoginScreenController`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.login_screen.LoginScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivy.uix.screenmanager.ScreenManager`.

    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        self.dialog = MDDialog()
        self.dialog.bind(on_dismiss=self.controller.reset_data_validation_status)
        self.model.add_observer(self)

    def show_dialog_wait(self) -> NoReturn:
        """Displays a wait dialog while the model is processing data."""

        self.dialog.auto_dismiss = False
        self.dialog.text = "Data validation..."
        self.dialog.open()

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        if self.model.data_validation_status:
            self.dialog.dismiss()
            toast("You have passed the verification successfully!")
        if self.model.data_validation_status is False:
            self.dialog.text = "Wrong data!"
            self.dialog.auto_dismiss = True
