import os.path
import datetime

from user import User, WrongEmailError
from load_data import LoadData
from task_collection import TaskCollection


class UserCollection:

    def __init__(self):
        self.users = []

    @property
    def users(self):
        return self.users

    @users.setter
    def users(self, users_):
        self.users = users_

    def __str__(self):
        s = ""
        for cur in self.users:
            s.join(str(cur))
        return s

    def read_users(self):
        users_list = LoadData.load("https://json.medrating.org/users")
        for cur in users_list:
            try:
                cur_user = User(
                    cur["id"], cur["name"],
                    cur["username"], cur["email"],
                    cur["company"]["name"], TaskCollection(cur["id"])
                )
                self.users.add(cur_user)
            except KeyError:
                print(f"The keys do not exist in user number {users_list.index(cur)+1}")
            except WrongEmailError:
                print(f"There are wrong email value in user number {users_list.index(cur)+1}")

    def write_users(self):
        dir_name = os.path.dirname(__file__) + '/tasks'
        try:
            os.mkdir(dir_name)
            print("The '/tasks' directory has been created.")
        except OSError:
            print("The '/tasks' directory already exist.")

        for cur in self.users:
            cur_path = f"{cur.username}.txt"
            if os.path.exists(cur_path):
                with open(cur_path, 'r') as cur_file:
                    str_date = cur_file.readline(2)
                    # os.path.getctime(path) -
                    # время создания файла (Windows),
                    # время последнего изменения файла (Unix).
                    str_date = str_date[str_date.find('>') + 2:str_date.find("\n")]
                    old_date = datetime.datetime.strptime(str_date, "%d-%m-%YT%H:%M")

                os.rename(cur_path,
                          f"old_{cur.username}_{old_date}.txt")

            with open(cur_path, 'w') as cur_file:
                cur_file.write(cur.create_report)
