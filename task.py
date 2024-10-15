class Task:
    def __init__(self, id, desc, status, priority):
        self._id = id
        self._desc = desc
        self._status = status
        self._priority = priority

    @property
    def id(self):
        return self._id

    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, new_desc):
        self._desc = new_desc
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, new_priority):
        self._priority = new_priority
    
    def mark_complete(self):
        self.status = 'complete'
        print(f"Task ID {self.id} marked as complete\n")
    
    def to_dict(self):
        return {
            'id': self._id,
            'desc': self._desc,
            'status': self._status,
            'priority': self._priority
        }