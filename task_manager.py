from task import Task
import json

class TaskManager():
    def __init__(self):
        self._task_list = []

    def load_task_list(self):
        try:
            with open("tasks.json", 'r') as f:
                load_list = json.load(f)
                for task in load_list:
                    x = Task(task['id'], task['desc'], task['status'], task['priority'])
                    self._task_list.append(x)
                print("Tasks loaded")
        except FileNotFoundError:
                print("No tasks loaded")

    def save_task_list(self):
        save_list =[]
        for task in self._task_list:
            x = task.to_dict()
            save_list.append(x)
        with open("tasks.json", 'w') as f:
            json.dump(save_list, f)

    def _convert_priority(self, priority):
        if priority == 1:
            return 'High'
        if priority == 2:
            return 'Medium'
        if priority == 3:
            return 'Low'
    
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
        self._print_single_task(task)
        confirm = input(
            f"\n"
            f"Confirm deletion: Y/N\n"
            f">>> "
        )
        if confirm.lower() in ['y','yes']:
            self._task_list.remove(task)
            print(f"Task {task.id} deleted")
            task.delete_task()
    
    def _print_single_task(self, task):
        print(
            f"ID: {task.id}\n"
            f"Description:\n{task.desc}\n"
            f"Priority: {self._convert_priority(task.priority)}\n"
            f"Status: {task.status.title()}"
            f"\n"
        )
    
    # def select_priority(self):
    #     priority = input(
    #                 f"Set priority: high, medium, low (defaults to low)\n"
    #                 f">>> "
    #             )
    #     if priority.lower() not in ['high', 'medium', 'h', 'm']:
    #         priority = 3
    #     elif priority.lower() in ['h', 'high']:
    #         priority = 1
    #     elif priority.lower() in ['m', 'medium']:
    #         priority = 2
    #     return priority
    
    def modify_task_description(self, task, desc):
        task.desc = desc

    def modify_task_priority(self, task, priority):
        task.priority = priority

    def list_tasks(self, status):
        print(
        f"{status.title()} tasks\n"
        f"----------------"
        )
        task_count = 0
        for task in self._task_list:
            if task.status == status:
                task_count += 1
                self._print_single_task(task)
        if task_count < 1:
            print("Empty\n")
    
    def order_tasks(self, priority):
        printed = False
        print(f"--- {self._convert_priority(priority)} Priority Tasks ---")
        for task in self._task_list:
            if task.priority == priority:
                self._print_single_task(task)
                printed = True
        if printed == False:
            print(f"--- No {self._convert_priority(priority)} Priority Tasks ---\n")
    
    def list_tasks_by_status(self):
        self.list_tasks('incomplete')
        self.list_tasks('complete')
        return

    def list_tasks_by_priority(self):
        self.order_tasks(1)
        self.order_tasks(2)
        self.order_tasks(3)
        return