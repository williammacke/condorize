from main_loop import _add_task
class Task:
    def __init__(self, f, *args, **kwargs):
        self._f = f
        self._args = args
        self._kwargs = kwargs
        #TODO: add random id for task
        self._id = "fixme"
        self._result = None
        self._job_id = None

class CondorFunction:
    def __init__(self, f):
        self._f = f

    def __call__(self, *args, **kwargs):
        t = Task(f, *args, **kwargs)
        _add_task(t)
        return t
