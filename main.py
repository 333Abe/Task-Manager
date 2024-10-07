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
    match priority:
        case 'h':
            priority = 'high'
        case 'm':
            priority ='medium'
    task_list.append({
        'id': id,
        'desc': desc,
        'status': 'incomplete',
        'priority': priority.title()
    })

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
                f"Priority: {task['priority']}"
                f"\n"
            )
    if task_count < 1:
        print("Empty\n")

def order_tasks():
    high_tasks = [task for task in task_list if task['priority'] == 'High']
    medium_tasks = [task for task in task_list if task['priority'] == 'Medium']
    low_tasks = [task for task in task_list if task['priority'] == 'Low']
    for task in high_tasks:
        print_single_task(task['id'])
    for task in medium_tasks:
        print_single_task(task['id'])
    for task in low_tasks:
        print_single_task(task['id'])

def print_single_task(id):
    for task in task_list:
        if task['id'] == id:
            print(
                f"ID: {task['id']}\n"
                f"Description:\n{task['desc']}\n"
                f"Priority: {task['priority']}\n"
                f"Status: {task['status'].title()}"
                f"\n"
            )

def complete_task(id):
    for task in task_list:
        if task['id'] == id:
            task['status'] = 'complete'
            print(f"Task ID {id} marked as complete\n")
            return
    print("Task does not exist")

def delete_task(id):
    for task in task_list:
        if task['id'] == id:
            if task['status'] == 'incomplete':
                confirm = input(
                    f"Specified task currently incomplete\n"
                    f"Confirm deletion: Y/N\n"
                    f">>> "
                )
                if confirm.lower() in ['y','yes']:
                    for task in task_list:
                        if task['id'] == id:
                            task_list.remove(task)
                            print(f"Task {id} deleted")
                            break
                elif confirm.lower() in ['n', 'no']:
                    print("Cancelling deletion...\n")
                else:
                    print("Unrecognised response: cancelling deletion...\n")
            else:
                task_list.remove(task)
                print(f"Task {id} deleted")

def select_priority():
    priority = input(
                f"Set priority: high, medium, low (defaults to low)\n"
                f">>> "
            )
    if priority.lower() not in ['high', 'medium', 'h', 'm']:
        priority = 'low'
    if priority.lower() == 'h':
        priority = 'high'
    if priority.lower() == 'm':
        priority = 'medium'
    return priority.title()

def update_task(id, key, value):
    for task in task_list:
        if task['id'] == id:
            task[key] = value

def modify_task(id):
    print_single_task(id)
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
        update_task(id, 'desc', desc)
    elif mod.lower() == 'p':
        priority = select_priority()
        update_task(id, 'priority', priority)
    else:
        print("Cancelling modification...")
        return
    
def validate_id(id):
    id_list = [task['id'] for task in task_list]
    try:
        if int(id) in id_list:
            return True
        print("No task with that ID")
        return False
    except ValueError:
        print("Invalid ID")
        return False

def save_task_list():
    with open("tasks.json", 'w') as f:
        json.dump(task_list, f)

def print_commands():
    print(f"Commands: list, add, complete, delete, modify, quit, help\n")

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
            add_task(desc, priority.lower())
            save_task_list()
        case 'complete' | 'c':
            id = input(
                f"Please type the ID of the task you wish to mark as complete:\n"
                f">>> "
            )
            if validate_id(id):
                complete_task(int(id))
            save_task_list()
        case 'delete' | 'd':
            id = input(
                f"Please type the ID of the task you wish to delete:\n"
                f">>> "
            )
            if validate_id(id):
                delete_task(int(id))
            save_task_list()
        case 'modify' | 'm':
            id = input(
                f"Please type the ID of the task you wish to modify:\n"
                f">>> "
            )
            if validate_id(id):
                modify_task(int(id))
            save_task_list()
        case 'quit' | 'q':
            print("Goodbye")
            break
        case 'help' | 'h':
            show_help()
        case 'order' | 'o':
            order_tasks()
        case _:
            print(f"Unrecognised command\n")
            print_commands()
            
            