class Task:

    def __init__(self, user_id_, title_, completed_):
        self.user_id = user_id_
        self.title = title_
        self.completed = completed_

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id_):
        self._user_id = user_id_

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_):
        if len(title_) > 48:
            title_ = ''.join([title_[:48], "..."])
        self._title = title_

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, completed_):
        if type(completed_) is bool:
            self._completed = completed_

    def __str__(self):
        return f"{self.title}"
