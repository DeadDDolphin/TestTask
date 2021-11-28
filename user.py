import datetime

from validate_email import validate_email

from task_collection import TaskCollection


class WrongEmailError(Exception):
    """Common base class for wrong email exception."""
    pass


class User:
    """Class User for storing user properties and creating a report about it

    Attributes
    ----------
    user_id: id
    fullname: str
    username: str
    email: str
    company: str
    tasks: TaskCollection

    Methods
    -------
    create_report():
        Creates a report based on user data.
    __init__(id_, fullname, username, email, company, tasks):
        Sets all the attributes for a user object
    __str__():
        returns the user description
    """

    def __init__(self, id_, fullname, username, email, company, tasks):
        """
        Sets all the attributes for a user object

        :param id_: user id
        :type id_: int
        :param fullname: user's fullname
        :type fullname: str
        :param username: username
        :type username: str
        :param email: user's email
        :type email: str
        :param company: name of user's company
        :type company: str
        :param tasks: all user tasks
        :type tasks: TaskCollection

        :raises WrongEmailError: if email is wrong
        """

        self.user_id = id_
        self.fullname = fullname
        self.username = username
        self.email = email
        self.company = company
        self.tasks = tasks

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, id_):
        self._user_id = id_

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, fullname_):
        self._fullname = fullname_

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username_):
        self._username = username_

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email_):
        if validate_email(email_):
            self._email = email_
        else:
            raise WrongEmailError

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company_):
        self._company = company_

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks_):
        if type(tasks_) is TaskCollection:
            self._tasks = tasks_

    def __str__(self):
        """

        :return: User's fullname
        """
        return f"This is {self.fullname}"

    def create_report(self) -> str:
        """
        Create report about user

        :rtype: str
        :return: report based on user data
        """
        d = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        rep = (
                f"Отчёт для {self.company}."
                f"\n{self.fullname} <{self.email}> {d}"
                f"\nВсего задач: {self.tasks.count}"

                f"\n\nЗавершённые задачи ({len(self.tasks.completed_tasks)}):"
                f"\n{self.tasks.completed_all()}"
                
                f"\n\nОставшиеся задачи ({len(self.tasks.remaining_tasks)}):"
                f"\n{self.tasks.remaining_all()}"
        )
        return rep
