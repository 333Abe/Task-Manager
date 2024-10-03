

task_list = []

def assign_id():
    id_list = [task['id'] for task in task_list]
    try:
        return max(id_list) + 1
    except ValueError:
        return 1

def add_task(desc):
    id = assign_id()
    task_list.append({
        'id': id,
        'desc': desc,
        'status': 'incomplete'
    })

def list_tasks():

    num_incomplete = [task['status'] for task in task_list].count('incomplete')
    num_complete = [task['status'] for task in task_list].count('complete')

    print(
        f"Incomplete tasks\n"
        f"----------------"
    )
    if num_incomplete > 0:
        for task in task_list:
            if task['status'] == 'incomplete':
                print(
                    f"ID: {task['id']}\n"
                    f"Description:\n{task['desc']}"
                    f"\n"
                )
    else:
        print("Empty")

    print(
        f"\n\n"
        f"Completed tasks\n"
        f"---------------"
    )
    if num_complete > 0:
        for task in task_list:
            if task['status'] == 'complete':
                print(
                    f"ID: {task['id']}\n"
                    f"Description:\n{task['desc']}"
                    f"\n"
                )
    else:
        print("Empty")

def complete_task(id):
    for task in task_list:
        if task['id'] == id:
            task['status'] = 'complete'
            print(f"Task ID {id} marked as complete\n")
            return
    print("Task does not exist")

def delete_task(task_id):
    for task in task_list:
        if task['id'] == task_id:
            if task['status'] == 'incomplete':
                confirm = input(
                    f"Specified task currently incomplete\n"
                    f"Confirm deletion: Y/N\n"
                    f">>> "
                )
                if confirm.lower() in ['y','yes']:
                    for task in task_list:
                        if task['id'] == task_id:
                            task_list.remove(task)
                            print(f"Task {task_id} deleted")
                            break
                elif confirm.lower() in ['n', 'no']:
                    print("Cancelling deletion...\n")
                else:
                    print("Unrecognised response: cancelling deletion...\n")
            else:
                task_list.remove(task)
                print(f"Task {task_id} deleted")

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

print(
    f"--------------- Task Manager --------------\n"
    f"Commands: list, add, complete, delete, quit\n"
)

while True:
    user_input = input(">>> ")
    match user_input.lower():
        case 'list' | 'l':
            list_tasks()
        case 'add' | 'a':
            desc = input(
                f"Write a task description\n"
                f">>> "
            )
            add_task(desc)
        case 'complete' | 'c':
            task_id = input(
                f"Please type the ID of the task you wish to mark as complete:\n"
                f">>> "
            )
            if validate_id(task_id):
                complete_task(int(task_id))
        case 'delete' | 'd':
            task_id = input(
                f"Please type the ID of the task you wish to delete:\n"
                f">>> "
            )
            if validate_id(task_id):
                delete_task(int(task_id))
        case 'quit' | 'q':
            print("Goodbye")
            break
        case _:
            print(
            f"Unrecognised command\n"
            f"Commands: list, add, complete, delete, quit\n"
            )