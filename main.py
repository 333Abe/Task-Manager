from help_info import show_help
from task_manager import TaskManager
from commands import AddTaskCommand, DeleteTaskCommand, CompleteTaskCommand, ListTasksByPriorityCommand, ListTasksByStatusCommand, ModifyTaskPriorityCommand, ModifyTaskDescriptionCommand

priority_dict = {
    'h': 1,
    'high': 1,
    'm': 2,
    'medium': 2,
    'l': 3,
    'low': 3
}
    
def validate_id(id):
    try:
        id = int(id)
        if id <= 0:
            raise ValueError
        return id
    except ValueError:
        return False

def print_commands():
    print(f"Commands: list, add, complete, delete, modify, order, quit, help\n")

def split_user_input(user_input):
    command_list = []
    command = ""
    str_char = False
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

def return_task(id):
    id = validate_id(id)
    if not id:
        print("Invalid id. Type 'help for more information.")
        return False
    task = task_manager.get_task_by_id(id)
    if not task:
        print("No task matches supplied id. Type 'help' for more information.")
        return False
    return task

def input_parser(user_input):
    command = split_user_input(user_input)
    
    if command[0] not in ['list', 'l', 'lp', 'ls', 'add', 'a', 'complete', 'c', 'modify', 'm', 'delete', 'd', 'quit', 'q', 'help', 'h']:
        print("Unrecognised command. Type 'help' for more information.")
        return True
    
    if command[0] == 'list' or command[0] == 'l':
        if len(command) == 2:
            if command[1] == 's' or command[1] == 'status':
                list_command = ListTasksByStatusCommand(task_manager)
                list_command.execute()
                return True
            if command[1] == 'p' or command[1] == 'priority':
                list_command = ListTasksByPriorityCommand(task_manager)
                list_command.execute()
                return True
        print("Invalid option(s) for 'list' function. Type 'help' for more information.")
        return True
        
    if command[0] == 'ls':
        list_command = ListTasksByStatusCommand(task_manager)
        list_command.execute()
        return True
    if command[0] == 'lp':
        list_command = ListTasksByPriorityCommand(task_manager)
        list_command.execute()
        return True

    if command[0] == 'add' or command[0] == 'a':
        if len(command) == 3 and command[2] in priority_dict.keys():
            desc = command[1]
            priority = priority_dict[command[2]]
            add_command = AddTaskCommand(task_manager, desc, priority)
            add_command.execute()
            task_manager.save_task_list()
            return True
        print("Invalid option(s) for 'add task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'complete' or command[0] == 'c':
        if len(command) == 2:
            id = command[1]
            task = return_task(id)
            if not task:
                return True
            complete_command = CompleteTaskCommand(task_manager, task)
            complete_command.execute()
            task_manager.save_task_list()
            return True
        print("Invalid option(s) for 'complete task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'modify' or command[0] == 'm':
        if len(command) == 4:
            id = command[1]
            task = return_task(id)
            if not task:
                return True
            if command[2] == 'd':
                desc = command[3]
                mod_desc_command = ModifyTaskDescriptionCommand(task_manager, task, desc)
                mod_desc_command.execute()
                task_manager.save_task_list()
                return True
            if command[2] == 'p' and command[3] in priority_dict.keys():
                priority = priority_dict[command[3]]
                mod_priority_command = ModifyTaskPriorityCommand(task_manager, task, priority)
                mod_priority_command.execute()
                task_manager.save_task_list()
                return True
        print("Invalid option(s) for 'modify task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'delete' or command[0] == 'd':
        if len(command) == 2:
            id = command[1]
            task = return_task(id)
            if not task:
                return True
            delete_command = DeleteTaskCommand(task_manager, task)
            delete_command.execute()
            task_manager.save_task_list()
            return True
        print("Invalid option(s) for 'delete task' function. Type 'help' for more information.")
        return True
    
    if command[0] == 'help' or command[0] == 'h':
        show_help()
    
    if command[0] == 'quit' or command[0] == 'q':
        return False
    

task_manager = TaskManager()
task_manager.load_task_list()
operate = True

print(f"------------------- Task Manager ------------------\n")
print_commands()

while True:
    user_input = input(">>> ")
    operate = input_parser(user_input)
    if operate == False:
        break
            
            