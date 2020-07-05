import os
from crontab import CronTab

user_name = os.environ.get("username")
path_var = os.environ.get("path to dbUpdater.py")
update_path_var = 'python3 '+path_var
cron_var = CronTab(user=user_name)
cron_job = cron_var.new(command=update_path_var)
cron_job.minute.every(5)
