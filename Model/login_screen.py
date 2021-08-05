# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.


import multitasking


multitasking.set_max_threads(10)


class LoginScreenModel:
    """Implements the logic of the user login screen."""

    def __init__(self, base):
        self.base = base
        # Data:
        #  {
        #      'login': 'User Login',
        #      'password': "12345",
        #  }
        self.user_data = {}
        self._data_validation_status = None
        self._observers = []

    @property
    def data_validation_status(self):
        return self._data_validation_status

    @data_validation_status.setter
    def data_validation_status(self, value):
        self._data_validation_status = value
        # We notify the View -
        # :class:`~View.LoginScreen.login_screen.LoginScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers()

    @multitasking.task
    def chek_data(self):
        """
        Get data from the database and compares this data with the data entered
        by the user.
        This method is completely asynchronous. It does not return any value.
        """

        data = self.base.get_data_from_base_users()
        data_validation_status = False

        for key in data:
            if data[key] == self.user_data:
                data_validation_status = True
                break
        self.data_validation_status = data_validation_status

    def set_user_data(self, key, value):
        """Sets a dictionary of data that the user enters."""

        self.user_data[key] = value

    def notify_observers(self):
        """
        The method that will be called on the observer when the model changes.
        """

        for observer in self._observers:
            observer.model_is_changed()

    def reset_data_validation_status(self):
        self.data_validation_status = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
