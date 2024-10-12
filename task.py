class Task:
    def __init__(self, id, desc, status, priority):
        self._id = id
        self._desc = desc
        self._status = status
        self._priority = priority

    def get_id(self):
        return self._id

    def get_desc(self):
        return self._desc
    
    def set_desc(self, new_desc):
        self._desc = new_desc
    
    def get_status(self):
        return self._status
    
    def set_status(self, new_status):
        self._status = new_status
    
    def get_priority(self):
        return self._priority
    
    def set_priority(self, new_priority):
        self._priority = new_priority
    
    def mark_complete(self):
        self.set_status('complete')
        print(f"Task ID {self.get_id()} marked as complete\n")
    
    def delete_task(self):
        del self