import datetime

from task_collection import TaskCollection


class User:

    def __init__(self, id_, fullname, username, email, company, tasks):
        self.user_id(id_)
        self.fullname(fullname)
        self.username(username)
        self.email(email)
        self.company(company)
        self.tasks(tasks)

    @property
    def user_id(self):
        return self.user_id

    @user_id.setter
    def user_id(self, id_):
        self.user_id = id_

    @property
    def fullname(self):
        return self.fullname

    @fullname.setter
    def fullname(self, fullname_):
        self.fullname = fullname_

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username_):
        self.username = username_

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email_):
        self.email = email_

    @property
    def company(self):
        return self.company

    @company.setter
    def company(self, company_):
        self.company = company_

    @property
    def tasks(self):
        return self.tasks

    @tasks.setter
    def tasks(self, tasks_):
        if type(tasks_) is TaskCollection:
            self.tasks = tasks_

    def __str__(self):
        return f"This is {self.fullname}"

    def create_report(self):
        d = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        rep = (
                f"Отчёт для {self.company}."
                f"\n{self.fullname} <{self.email}> {d}"
                f"\nВсего задач: {self.tasks.count}"

                f"\n\nЗавершённые задачи ({len(self.tasks.completed_tasks)}): {self.tasks.completed_all}"
                
                f"\n\nОставшиеся задачи ({len(self.tasks.remaining_tasks)}): {self.tasks.remaining_all}"
        )
        return rep
