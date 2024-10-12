from task import Task
import json

class TaskManager():
    def __init__(self, task_list):
        self._task_list = task_list

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
    
    def list_tasks(self, status):
        print(
        f"{status.title()} tasks\n"
        f"----------------"
        )
        task_count = 0
        for task in self._task_list:
            if task.get_status() == status:
                task_count += 1
                print(
                    f"ID: {task.get_id()}\n"
                    f"Description:\n{task.get_desc()}\n"
                    f"Priority: {self._convert_priority(task.get_priority())}"
                    f"\n"
                )
        if task_count < 1:
            print("Empty\n")
    
    def _assign_id(self):
        id_list = [task.get_id() for task in self._task_list]
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
            if task.get_id() == id:
                return task
        print("No task with that ID")
        return None
    
    def delete_task(self, task):
        if task.get_status() == 'incomplete':
            confirm = input(
                f"Specified task currently incomplete\n"
                f"Confirm deletion: Y/N\n"
                f">>> "
            )
            if confirm.lower() in ['y','yes']:
                self._task_list.remove(task)
                print(f"Task {task.get_id()} deleted")
                task.delete_task()
            elif confirm.lower() in ['n', 'no']:
                print("Cancelling deletion...\n")
            else:
                print("Unrecognised response: cancelling deletion...\n")
        else:
            self._task_list.remove(task)
            print(f"Task {task.get_id()} deleted")
            task.delete_task()
    
    def _print_single_task(self, task):
        print(
            f"ID: {task.get_id()}\n"
            f"Description:\n{task.get_desc()}\n"
            f"Priority: {self._convert_priority(task.get_priority())}\n"
            f"Status: {task.get_status().title()}"
            f"\n"
        )
    
    def select_priority(self):
        priority = input(
                    f"Set priority: high, medium, low (defaults to low)\n"
                    f">>> "
                )
        if priority.lower() not in ['high', 'medium', 'h', 'm']:
            priority = 3
        elif priority.lower() in ['h', 'high']:
            priority = 1
        elif priority.lower() in ['m', 'medium']:
            priority = 2
        return priority
    
    def modify_task(self, task):
        self._print_single_task(task)
        mod = input(
            f"Would you like to change the description, or the priority?\n"
            f"Type d or p, or anything else to cancel\n"
            f">>> "
        )
        if mod.lower() == 'd':
            desc = input(
                f"Enter a new description"
                f">>> "
            )
            task.set_desc(desc)
        elif mod.lower() == 'p':
            priority = self.select_priority()
            task.set_priority(priority)
        else:
            print("Cancelling modification...")
            return
    
    def order_tasks(self, priority):
        printed = False
        print(f"--- {self._convert_priority(priority)} Priority Tasks ---")
        for task in self._task_list:
            if task.get_priority() == priority:
                self._print_single_task(task)
                printed = True
        if printed == False:
            print(f"--- No {self._convert_priority(priority)} Priority Tasks ---\n")