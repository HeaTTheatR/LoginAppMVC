# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.login_screen import LoginScreenModel

from Controller.login_screen import LoginScreenController

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
}
