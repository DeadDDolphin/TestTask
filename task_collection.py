from task import Task
from load_data import LoadData


class KeyErrorException(Exception):
    """
    Class for equal KeyError by index

    Attributes
    ----------
    index: int

    Methods
    -------
    __init__(index)
    __hash__():
        overwrite for hash. The hash is calculated
        depending on the index
    __eq__():
        overwrite for eq.

    """

    def __init__(self, index):
        self.index = index

    def __hash__(self):
        return self.index

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            return True
        return False


class TaskCollection:
    """
    Class for describe collection of tasks.

    Class attributes
    ----------------
    exceptions: set
        Set for KeyError exceptions

    Attributes
    ----------
    user_id: int
    completed_tasks: list
    remaining_tasks: list
    count: int

    Methods
    -------
    __init__():
        Creates empty lists.
        Calls the read_tasks() method to fill the lists.
        Calculates the count of tasks.
    completed_all():
        :rtype: str
        :return: string contains all titles of completed tasks
    remaining_all():
        :rtype: str
        :return: string contains all titles of remaining tasks
    read_tasks():
        Reads the tasks from url
    """
    exceptions = set()

    def __init__(self, id_):
        self.user_id = id_
        self.completed_tasks = []
        self.remaining_tasks = []
        self.read_tasks()
        self.count = len(self.completed_tasks) + len(self.remaining_tasks)

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, id_):
        self._user_id = id_

    @property
    def completed_tasks(self):
        return self._completed_tasks

    @completed_tasks.setter
    def completed_tasks(self, tasks):
        if type(tasks) is list:
            self._completed_tasks = tasks

    @property
    def remaining_tasks(self):
        return self._remaining_tasks

    @remaining_tasks.setter
    def remaining_tasks(self, tasks):
        if type(tasks) is list:
            self._remaining_tasks = tasks

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count_):
        self._count = count_

    def completed_all(self) -> str:
        """
        Joins all completed titles into a single string
        :rtype: str
        :return: all completed titles
        """

        s = []
        for cur in self.completed_tasks:
            s.append(cur.title)
        return '\n'.join(s)

    def remaining_all(self) -> str:
        """
        Joins all remaining titles into a single string
        :rtype: str
        :return: all remaining titles
        """

        s = []
        for cur in self.remaining_tasks:
            s.append(cur.title)
        return '\n'.join(s)

    def read_tasks(self):
        """
        Load data from url.
        Read all tasks with userId equal to the user ID of concrete instance.
        Append KeyErrorException into exceptions
        if the task don't have the required keys
        :return: None
        """
        task_list = LoadData.load("https://json.medrating.org/todos")
        for cur in task_list:
            try:
                if cur["userId"] == self.user_id:
                    task = Task(cur["userId"],
                                cur["title"],
                                cur["completed"])
                    if task.completed:
                        self.completed_tasks.append(task)
                    else:
                        self.remaining_tasks.append(task)
            except KeyError:
                exc = KeyErrorException(task_list.index(cur))
                TaskCollection.exceptions.add(exc)
