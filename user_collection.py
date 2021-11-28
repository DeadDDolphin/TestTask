import os.path
import shutil

from user import User, WrongEmailError
from load_data import LoadData
from task_collection import TaskCollection


class UserCollection:
    """
    Class for user collection

    Attributes
    ----------
    users: list

    Methods
    -------
    __init__():
        create empty list of users
    __str__():
        returns the full names of users
    add_user(user):
        add user to list
    read_users():
        reads data and creates users from url
    write_users():
        writes user reports to files
    """

    def __init__(self):
        self.users = []

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users_):
        self._users = users_

    def __str__(self):
        s = ""
        for cur in self.users:
            s.join(str(cur))
        return s

    def add_user(self, user):
        """
        Add user to list
        :param user:
        :return: None
        """
        self.users.append(user)

    def read_users(self):
        """
        Load data from url.
        For each dataset creates a user instance and adds to the list
        Prints KeyError exceptions
        :return: None
        """
        users_list = LoadData.load("https://json.medrating.org/users")
        for cur in users_list:
            try:
                cur_user = User(
                    cur["id"], cur["name"],
                    cur["username"], cur["email"],
                    cur["company"]["name"], TaskCollection(cur["id"])
                )
                self.add_user(cur_user)
            except KeyError:
                print(f"The keys do not exist in user number {users_list.index(cur)+1}")
            except WrongEmailError:
                print(f"There are wrong email value in user number {users_list.index(cur)+1}")
        if TaskCollection.exceptions:
            print(TaskCollection.exceptions)

    def write_users(self):
        """
        Create the 'tasks' directory if not exist.
        For each user instance create new file with report.
        If file already exist rename old file
        :return: None
        """
        dir_name = os.path.dirname(__file__) + '/tasks'
        try:
            os.mkdir(dir_name)
            print("The '/tasks' directory has been created.")
        except OSError:
            print("The '/tasks' directory already exist.")

        for cur in self.users:
            cur_path = f"{dir_name}/{cur.username}.txt"
            if os.path.exists(cur_path):
                old_date = LoadData.get_date_from_file(cur_path)
                old_path = f"{dir_name}/old_{cur.username}_{old_date}.txt"
                shutil.copy(cur_path, old_path)

            with open(cur_path, 'w') as cur_file:
                cur_file.write(cur.create_report())
