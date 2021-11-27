from task import Task
from load_data import LoadData


class TaskCollection:

    def __init__(self, id_):
        self.user_id(id_)
        self.completed_tasks = []
        self.remaining_tasks = []
        self.read_tasks()
        self.count(len(self.completed_tasks) + len(self.remaining_tasks))

    @property
    def user_id(self):
        return self.user_id

    @user_id.setter
    def user_id(self, id_):
        self.user_id = id_

    @property
    def completed_tasks(self):
        return self.completed_tasks

    @completed_tasks.setter
    def completed_tasks(self, tasks):
        if type(tasks) is list:
            self.completed_tasks = tasks

    @property
    def remaining_tasks(self):
        return self.remaining_tasks

    @remaining_tasks.setter
    def remaining_tasks(self, tasks):
        if type(tasks) is list:
            self.remaining_tasks = tasks

    @property
    def count(self):
        return self.count

    @count.setter
    def count(self, count_):
        self.count = count_

    def completed_all(self):
        s = ""
        for cur in self.completed_tasks:
            '\n'.join([s, cur.title])
        return s

    def remaining_all(self):
        s = ""
        for cur in self.remaining_tasks:
            '\n'.join([s, cur.title])
        return s

    def read_tasks(self):
        task_list = LoadData.load("https://json.medrating.org/todos")
        for cur in task_list:
            try:
                if cur["userId"] == self.user_id:
                    task = Task(cur["userId"], cur["title"], cur["completed"])
            except KeyError:
                print(f"The keys do not exist in item number {task_list.index(cur)}")
            else:
                if task.completed:
                    self.completed_tasks.add(task)
                else:
                    self.remaining_tasks.add(task)
