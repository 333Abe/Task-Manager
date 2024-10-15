from task import Task
import json

class TaskManager():
    def __init__(self):
        self._task_list = []

    PRIORITY_MAP = {
        1: 'High',
        2: 'Medium',
        3: 'Low'
    }

    def load_task_list(self):
        try:
            with open("tasks.json", 'r') as f:
                load_list = json.load(f)
                for task in load_list:
                    x = Task(task['id'], task['desc'], task['status'], task['priority'])
                    self._task_list.append(x)
                return "Tasks loaded"
        except FileNotFoundError:
                return "No tasks loaded"

    def save_task_list(self):
        save_list =[]
        for task in self._task_list:
            x = task.to_dict()
            save_list.append(x)
        with open("tasks.json", 'w') as f:
            json.dump(save_list, f)
    
    def _assign_id(self):
        id_list = [task.id for task in self._task_list]
        try:
            return max(id_list) + 1
        except ValueError:
            return 1

    def add_task(self, desc, priority):
        id = self._assign_id()
        task = Task(id, desc,'incomplete', priority )
        self._task_list.append(task)
    
    def get_task_by_id(self, id):
        for task in self._task_list:
            if task.id == id:
                return task
        return None
    
    def delete_task(self, task):
        self._task_list.remove(task)
        task.delete_task()
    
    def print_single_task(self, task):
        print(
            f"ID: {task.id}\n"
            f"Description:\n{task.desc}\n"
            f"Priority: {self.PRIORITY_MAP[task.priority]}\n"
            f"Status: {task.status.title()}"
            f"\n"
        )
    
    def modify_task_description(self, task, desc):
        task.desc = desc

    def modify_task_priority(self, task, priority):
        task.priority = priority

    def mark_complete(self, task):
        task.mark_complete()

    def list_tasks(self, status):
        print(
        f"{status.title()} tasks\n"
        f"----------------"
        )
        task_count = 0
        for task in self._task_list:
            if task.status == status:
                task_count += 1
                self.print_single_task(task)
        if task_count < 1:
            print("Empty\n")
    
    def order_tasks(self, priority):
        printed = False
        print(f"--- {self.PRIORITY_MAP[priority]} Priority Tasks ---")
        for task in self._task_list:
            if task.priority == priority:
                self.print_single_task(task)
                printed = True
        if printed == False:
            print(f"--- No {self.PRIORITY_MAP[priority]} Priority Tasks ---\n")
    
    def list_tasks_by_status(self):
        self.list_tasks('incomplete')
        self.list_tasks('complete')
        return

    def list_tasks_by_priority(self):
        self.order_tasks(1)
        self.order_tasks(2)
        self.order_tasks(3)
        return