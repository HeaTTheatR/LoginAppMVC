from typing import NoReturn

from View.LoginScreen.login_screen import LoginScreenView


class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.

    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = LoginScreenView(controller=self, model=self.model)

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

        self.model.set_user_data(key, value)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

        self.view.show_dialog_wait()
        self.model.chek_data()

    def reset_data_validation_status(self, *args) -> NoReturn:
        self.model.reset_data_validation_status()

    def get_view(self) -> LoginScreenView:
        return self.view
