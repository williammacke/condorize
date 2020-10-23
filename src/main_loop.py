from collections import deque
import os


#TODO: add mutex to prevent race conditions


_tasks = deque()
_max_jobs = 0
_running_tasks = {}
_complete_tasks = {}
_working_dir = ""


def init():
    raise NotImplementedError


def close():
    raise NotImplementedError


def _submit_job(task):
    raise NotImplementedError


def _add_task(t):
    _tasks.append(t)


def _main_loop():
    complete_dir = os.join_path(_working_dir, "results/")
    for k in _running_jobs:
        #TODO: check for complete tasks
    while _tasks and len(_running_jobs) < _max_jobs:
        t = _tasks.pop_left()
        _running_tasks[t._id] = t
        _submit_job(t)
    #TODO: add sleep statement
