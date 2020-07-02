import os
from crontab import CronTab

user_name = os.environ.get("login_user_name")
path_var = os.environ.get("path_for_interval_update_database")
update_path_var = 'python3 '+path_var
cron_var = CronTab(user=user_name)
cron_job = cron_var.new(command=update_path_var)
cron_job.minute.every(5)
 
cron_var.write()
