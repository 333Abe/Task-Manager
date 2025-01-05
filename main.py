from help_info import show_help
from task_manager import TaskManager
from task import Task
from commands import Command
from commands import AddTaskCommand, DeleteTaskCommand, CompleteTaskCommand, ListTasksByPriorityCommand, ListTasksByStatusCommand, ModifyTaskPriorityCommand, ModifyTaskDescriptionCommand

PRIORITY_MAP: dict[str | int] = {
    'h': 1,
    'high': 1,
    'm': 2,
    'medium': 2,
    'l': 3,
    'low': 3
}
    
def validate_id(task_id: str) -> int | bool:
    try:
        task_id: int = int(task_id)
        if task_id <= 0:
            raise ValueError
        return task_id
    except ValueError:
        return False

def print_commands() -> None:
    print(f"Commands: list, add, complete, delete, modify, order, quit, help\n")

def split_user_input(user_input: str) -> list[str]:
    command_list: list = []
    command: str = ""
    str_char: bool | str = False
    for char in user_input:
        if char == " " and str_char == False:
            command_list.append(command)
            command = ""
            continue
        if char == '"' and str_char == False:
            str_char = '"'
            continue
        if char == "'" and str_char == False:
            str_char = "'"
            continue
        if char == str_char:
            str_char = False
            continue
        command += char
    command_list.append(command)
    return command_list

def return_task(task_id: str, task_manager: TaskManager) -> Task | bool:
    task_id: int | bool = validate_id(task_id)
    if not task_id:
        print("Invalid id. Type 'help for more information.")
        return False
    task: Task | None = task_manager.get_task_by_id(task_id)
    if not task:
        print("No task matches supplied id. Type 'help' for more information.")
        return False
    return task

def input_parser(user_input: str, task_manager: TaskManager) -> bool:
    command: list[str] = split_user_input(user_input)
    
    if command[0] not in ['list', 'l', 'lp', 'ls', 'add', 'a', 'complete', 'c', 'modify', 'm', 'delete', 'd', 'quit', 'q', 'help', 'h']:
        print("Unrecognised command. Type 'help' for more information.")
        return True
    
    if command[0] == 'list' or command[0] == 'l':
        if len(command) == 2:
            if command[1] == 's' or command[1] == 'status':
                list_command: Command = ListTasksByStatusCommand(task_manager)
                list_command.execute()
                return True
            if command[1] == 'p' or command[1] == 'priority':
                list_command: Command = ListTasksByPriorityCommand(task_manager)
                list_command.execute()
                return True
        print("Invalid option(s) for 'list' function. Type 'help' for more information.")
        return True
        
    if command[0] == 'ls':
        list_command: Command = ListTasksByStatusCommand(task_manager)
        list_command.execute()
        return True
    
    if command[0] == 'lp':
        list_command: Command = ListTasksByPriorityCommand(task_manager)
        list_command.execute()
        return True

    if command[0] == 'add' or command[0] == 'a':
        if len(command) == 3 and command[2] in PRIORITY_MAP.keys():
            desc: str = command[1]
            priority: int = PRIORITY_MAP[command[2]]
            add_command: Command = AddTaskCommand(task_manager, desc, priority)
            add_command.execute()
            return True
        print("Invalid option(s) for 'add task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'complete' or command[0] == 'c':
        if len(command) == 2:
            task_id: str = command[1]
            task: Task | bool = return_task(task_id, task_manager)
            if not task:
                return True
            complete_command: Command = CompleteTaskCommand(task_manager, task)
            complete_command.execute()
            return True
        print("Invalid option(s) for 'complete task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'modify' or command[0] == 'm':
        if len(command) == 4:
            task_id: str = command[1]
            task: Task | bool = return_task(task_id, task_manager)
            if not task:
                return True
            if command[2] == 'd':
                desc: str = command[3]
                mod_desc_command: Command = ModifyTaskDescriptionCommand(task_manager, task, desc)
                mod_desc_command.execute()
                return True
            if command[2] == 'p' and command[3] in PRIORITY_MAP.keys():
                priority: int = PRIORITY_MAP[command[3]]
                mod_priority_command: Command = ModifyTaskPriorityCommand(task_manager, task, priority)
                mod_priority_command.execute()
                return True
        print("Invalid option(s) for 'modify task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'delete' or command[0] == 'd':
        if len(command) == 2:
            task_id: str = command[1]
            task: Task | bool = return_task(task_id, task_manager)
            if not task:
                return True
            task_manager.print_single_task(task)
            confirm: str = input(
                f"\n"
                f"Confirm deletion: Y/N\n"
                f">>> "
            )
            if confirm.lower() in ['y','yes']:
                delete_command: Command = DeleteTaskCommand(task_manager, task)
                delete_command.execute()
            return True
        print("Invalid option(s) for 'delete task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'help' or command[0] == 'h':
        show_help()
    
    if command[0] == 'quit' or command[0] == 'q':
        return False
    
def main() -> None:
    task_manager: TaskManager = TaskManager()
    print(task_manager.load_task_list())
    operate = True

    print(f"------------------- Task Manager ------------------\n")
    print_commands()

    while True:
        user_input: str = input(">>> ")
        operate: bool = input_parser(user_input, task_manager)
        task_manager.save_task_list()
        if operate == False:
            break

if __name__ == '__main__':
    main()
            