class Usuario:

    # Los parametros pueden no ser nesesarios(como el id en INSERT), por eso son "None"
    def __init__(self, id_user = None, user_name = None, user_password = None):
        self._id_user = id_user
        self._user_name = user_name
        self._user_password = user_password

    @property
    def id_user(self):
        return self._id_user
    
    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user 

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @property
    def user_password(self):
        return self._user_password    

    @user_password.setter
    def user_password(self, user_password):
        self._user_password = user_password

    def __str__(self):
        return f"ID: {self._id_user} - USERNAME:{self._user_name} - PASSWORD: {self._user_password}"
