from collections import deque
import os
import pickle


#TODO: add mutex to prevent race conditions


_tasks = deque()
_max_jobs = 0
_running_tasks = {}
_complete_tasks = {}
_working_dir = ""


def init(working_dir, max_jobs=10):
    _working_dir = working_dir
    _max_jobs = max_jobs
    raise NotImplementedError


def close():
    raise NotImplementedError


def _submit_job(task):
    filename = os.join_path(_working_dir, "job_tasks/", (task._id+".job"))
    with open(filename, 'wb') as f:
        pickle.dump(task, f)
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
