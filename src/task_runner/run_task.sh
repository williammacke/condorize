source ~/.bashrc
conda activate $1
python -m condor.task_runner.run_task $2 $3
