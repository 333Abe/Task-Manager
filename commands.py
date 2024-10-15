from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddTaskCommand(Command):
    def __init__(self, task_manager, desc, priority):
        self.task_manager = task_manager
        self.desc = desc
        self.priority = priority
    
    def execute(self):
        self.task_manager.add_task(self.desc, self.priority)

class CompleteTaskCommand(Command):
    def __init__(self, task_manager, task):
        self.task_manager = task_manager
        self.task = task
    
    def execute(self):
        self.task_manager.mark_complete(self.task)

class DeleteTaskCommand(Command):
    def __init__(self, task_manager, task):
        self.task_manager = task_manager
        self.task = task
    
    def execute(self):
        self.task_manager.delete_task(self.task)

class ListTasksByStatusCommand(Command):
    def __init__(self, task_manager):
        self.task_manager = task_manager
    
    def execute(self):
        self.task_manager.list_tasks_by_status()

class ListTasksByPriorityCommand(Command):
    def __init__(self, task_manager):
        self.task_manager = task_manager
    
    def execute(self):
        self.task_manager.list_tasks_by_priority()

class ModifyTaskPriorityCommand(Command):
    def __init__(self, task_manager, task, new_priority):
        self.task_manager = task_manager
        self.task = task
        self.new_priority = new_priority

    def execute(self):
        self.task_manager.modify_task_priority(self.task, self.new_priority)

class ModifyTaskDescriptionCommand(Command):
    def __init__(self, task_manager, task, new_desc):
        self.task_manager = task_manager
        self.task = task
        self.new_desc = new_desc

    def execute(self):
        self.task_manager.modify_task_description(self.task, self.new_desc)


