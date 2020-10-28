from collections import deque
import os
import pickle
import threading
import time


#TODO: add mutex to prevent race conditions


_tasks = deque()
_max_jobs = 0
_running_tasks = {}
_complete_tasks = {}
_working_dir = ""
_running = False
_thread = None


def init(working_dir, max_jobs=10):
    global _working_dir
    global _max_jobs
    global _running
    global _thread
    _working_dir = working_dir
    _max_jobs = max_jobs
    _running = True
    _thread = threading.Thread(target=_main_loop)
    _thread.start()




def close():
    _running = False
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
    while _running:
        for n in os.listdir(complete_dir):
            nid = n.split('_')[0]
            with open(complete_dir + n, 'rb') as f:
                result = pickle.load(f)
            _running_tasks[nid].result = result
            del _running_tasks[nid]
        while _tasks and len(_running_jobs) < _max_jobs:
            t = _tasks.pop_left()
            _running_tasks[t._id] = t
            _submit_job(t)
        time.sleep(5)
