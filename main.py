import json
from help_info import show_help

def assign_id():
    id_list = [task['id'] for task in task_list]
    try:
        return max(id_list) + 1
    except ValueError:
        return 1

def add_task(desc, priority):
    id = assign_id()
    task_list.append({
        'id': id,
        'desc': desc,
        'status': 'incomplete',
        'priority': priority
    })

def convert_priority(priority):
    if priority == 1:
        return 'High'
    if priority == 2:
        return 'Medium'
    if priority == 3:
        return 'Low'

def list_tasks(status):
    print(
    f"{status.title()} tasks\n"
    f"----------------"
    )
    task_count = 0
    for task in task_list:
        if task['status'] == status:
            task_count += 1
            print(
                f"ID: {task['id']}\n"
                f"Description:\n{task['desc']}\n"
                f"Priority: {convert_priority(task['priority'])}"
                f"\n"
            )
    if task_count < 1:
        print("Empty\n")

def order_tasks(priority):
    printed = False
    print(f"--- {convert_priority(priority)} Priority Tasks ---")
    for task in task_list:
        if task['priority'] == priority:
            print_single_task(task)
            printed = True
    if printed == False:
        print(f"--- No {convert_priority(priority)} Priority Tasks ---\n")

def print_single_task(task):
    print(
        f"ID: {task['id']}\n"
        f"Description:\n{task['desc']}\n"
        f"Priority: {convert_priority(task['priority'])}\n"
        f"Status: {task['status'].title()}"
        f"\n"
    )

def complete_task(task):
    task['status'] = 'complete'
    print(f"Task ID {task['id']} marked as complete\n")
    return

def delete_task(task):
    if task['status'] == 'incomplete':
        confirm = input(
            f"Specified task currently incomplete\n"
            f"Confirm deletion: Y/N\n"
            f">>> "
        )
        if confirm.lower() in ['y','yes']:
            task_list.remove(task)
            print(f"Task {task['id']} deleted")
        elif confirm.lower() in ['n', 'no']:
            print("Cancelling deletion...\n")
        else:
            print("Unrecognised response: cancelling deletion...\n")
    else:
        task_list.remove(task)
        print(f"Task {task['id']} deleted")

def select_priority():
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

def update_task(task, key, value):
    task[key] = value

def modify_task(task):
    print_single_task(task)
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
        update_task(task, 'desc', desc)
    elif mod.lower() == 'p':
        priority = select_priority()
        update_task(task, 'priority', priority)
    else:
        print("Cancelling modification...")
        return
    
def get_task_by_id(id):
    for task in task_list:
        if task['id'] == id:
            return task
    print("No task with that ID")
    return None
    
def validate_id(id):
    try:
        id = int(id)
        if id <= 0:
            raise ValueError
        return id
    except ValueError:
        print("Invalid ID")
        return False

def save_task_list():
    with open("tasks.json", 'w') as f:
        json.dump(task_list, f)

def print_commands():
    print(f"Commands: list, add, complete, delete, modify, order, quit, help\n")

try:
    with open("tasks.json", 'r') as f:
        task_list = json.load(f)
except FileNotFoundError:
        task_list = []

print(f"------------------- Task Manager ------------------\n")
print_commands()


while True:
    user_input = input(">>> ")
    match user_input.lower():
        case 'list' | 'l':
            list_tasks('incomplete')
            list_tasks('complete')
        case 'add' | 'a':
            desc = input(
                f"Write a task description\n"
                f">>> "
            )
            priority = select_priority()
            add_task(desc, priority)
            save_task_list()
        case 'complete' | 'c':
            id = input(
                f"Please type the ID of the task you wish to mark as complete:\n"
                f">>> "
            )
            id = validate_id(id)
            if not id:
                continue
            task = get_task_by_id(id)
            if not task:
                continue
            complete_task(task)
            save_task_list()
        case 'delete' | 'd':
            id = input(
                f"Please type the ID of the task you wish to delete:\n"
                f">>> "
            )
            id = validate_id(id)
            if not id:
                continue
            task = get_task_by_id(id)
            if not task:
                continue
            delete_task(task)
            save_task_list()
        case 'modify' | 'm':
            id = input(
                f"Please type the ID of the task you wish to modify:\n"
                f">>> "
            )
            id = validate_id(id)
            if not id:
                continue
            task = get_task_by_id(id)
            if not task:
                continue
            modify_task(task)
            save_task_list()
        case 'quit' | 'q':
            print("Goodbye")
            break
        case 'help' | 'h':
            show_help()
        case 'order' | 'o':
            order_tasks(1)
            order_tasks(2)
            order_tasks(3)
        case _:
            print(f"Unrecognised command\n")
            print_commands()
            
            