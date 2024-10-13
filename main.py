import json
from help_info import show_help
from task_manager import TaskManager
    
def validate_id(id):
    try:
        id = int(id)
        if id <= 0:
            raise ValueError
        return id
    except ValueError:
        print("Invalid ID")
        return False

def print_commands():
    print(f"Commands: list, add, complete, delete, modify, order, quit, help\n")

task_manager = TaskManager()
task_manager.load_task_list()

print(f"------------------- Task Manager ------------------\n")
print_commands()

while True:
    user_input = input(">>> ")
    match user_input.lower():
        case 'list' | 'l':
            task_manager.list_tasks('incomplete')
            task_manager.list_tasks('complete')
        case 'add' | 'a':
            desc = input(
                f"Write a task description\n"
                f">>> "
            )
            priority = task_manager.select_priority()
            task_manager.add_task(desc, priority)
            task_manager.save_task_list()
        case 'complete' | 'c':
            id = input(
                f"Please type the ID of the task you wish to mark as complete:\n"
                f">>> "
            )
            id = validate_id(id)
            if not id:
                continue
            task = task_manager.get_task_by_id(id)
            if not task:
                continue
            task.mark_complete()
            task_manager.save_task_list()
        case 'delete' | 'd':
            id = input(
                f"Please type the ID of the task you wish to delete:\n"
                f">>> "
            )
            id = validate_id(id)
            if not id:
                continue
            task = task_manager.get_task_by_id(id)
            if not task:
                continue
            task_manager.delete_task(task)
            task_manager.save_task_list()
        case 'modify' | 'm':
            id = input(
                f"Please type the ID of the task you wish to modify:\n"
                f">>> "
            )
            id = validate_id(id)
            if not id:
                continue
            task = task_manager.get_task_by_id(id)
            if not task:
                continue
            task_manager.modify_task(task)
            task_manager.save_task_list()
        case 'quit' | 'q':
            print("Goodbye")
            break
        case 'help' | 'h':
            show_help()
        case 'order' | 'o':
            task_manager.order_tasks(1)
            task_manager.order_tasks(2)
            task_manager.order_tasks(3)
        case _:
            print(f"Unrecognised command\n")
            print_commands()
            
            